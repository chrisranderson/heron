from config import config
from util import *
from heron_builtins import *
from math import *
from evaluate import *

'''
        mu ~ uniform_continuous(-10, 10)
        x ~ normal(mu, 1)

        data = [x=1, x=2, x=3, x=4, x=5]

        plot(p(mu|x:data))
'''
def evaluate_model_definitions(model_definitions):
    computed_values = {}

    def evaluate_argument(argument):
        if is_number(argument):
            return argument
        else:
            try:
                return computed_values[argument]
            except KeyError:
                return evaluate_definition(argument)

    def evaluate_definition(variable_name):
        distribution, arguments = model_definitions[variable_name]
        evaluated_arguments = []
        for argument in arguments:
            evaluated_arguments.append(evaluate_argument(argument))
        return distribution(*evaluated_arguments)

    for variable_name, (distribution, arguments) in model_definitions.items():
        computed_values[variable_name] = evaluate_definition(variable_name)

    return computed_values

def get_prior_probability(variable_assignments, environment):
    latent_variable_name = environment.latent_variables[0]
    latent_value = variable_assignments[latent_variable_name]
    function, arguments = environment.get_model_definition(latent_variable_name)
    arguments.append(latent_value)
    return log(function(*arguments))

def get_likelihood(variable_assignments, environment):
    likelihood = 0
    for child, parents in environment.child_to_parent_dependencies.items():
        for parent in parents:
            function, arguments = environment.get_model_definition(parent)
            arguments[arguments.index(child)] = variable_assignments[child]
            data = environment.get_model_observation(parent)
            for datum in data:
                try:
                    likelihood += log(function(*list_append(arguments, datum)))
                except ValueError as e:
                    likelihood += -1000

    return likelihood

def get_posterior(variable_assignments, environment):
    prior_probability = get_prior_probability(variable_assignments, environment)
    likelihood = get_likelihood(variable_assignments, environment)
    posterior = likelihood + prior_probability
    return posterior

def propose(old_variable_assignments):
    return {var_name: normal(value, 1) for (var_name, value) in old_variable_assignments.items()}
# p(mu | x:data)
# p(a | b) = (p(a) * p(b | a)) / p(b)

# p(mu) * p(x | mu) / p(x)
def generate_samples(environment):
    environment.add_dependency_graph()
    samples = []

    old_values = evaluate_model_definitions(environment.model_definitions)
    old_posterior = get_posterior(old_values, environment)

    samples.append(old_values)
    sample_count = 0
    while sample_count < config['sample_count']:
        if sample_count % 100 == 0:
            print("\rGenerating samples... {} / {}".format(sample_count, config['sample_count']), end='')

        new_values = propose(old_values)
        new_posterior = get_posterior(new_values, environment)
        acceptance_ratio = new_posterior - old_posterior

        if acceptance_ratio >= 1 or log(np.random.rand()) < acceptance_ratio:
            old_values = new_values
            old_posterior = new_posterior

        samples.append(old_values)
        sample_count += 1

    print("\rGenerating samples... {} / {}".format(sample_count, config['sample_count']), end='\n')

    if len(environment.latent_variables) == 1:
        samples =  [[value for (var_name, value) in pair.items() if var_name in environment.latent_variables][0] for pair in samples]
    else:
        samples =  [{var_name: value for (var_name, value) in pair.items() if var_name in environment.latent_variables} for pair in samples]

    print(np.mean(samples))
    return samples

if __name__ == "__main__":
    code = '''
        mu ~ uniform_continuous(-10, 10)
        x ~ normal(mu, 1)
        data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
        plot(p(mu | x:data))
    '''

    evaluate(code)


