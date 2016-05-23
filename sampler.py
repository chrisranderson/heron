from config import config
from util import *
from heron_builtins import *

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
    return function(*arguments)

def get_likelihood(variable_assignments, environment):
    for child, parents in environment.child_to_parent_dependencies.items():


# p(mu | x:data)
# p(a | b) = (p(a) * p(b | a)) / p(b)

# p(mu) * p(x | mu) / p(x)
def generate_samples(environment):
    environment.add_dependency_graph()

    old_values = evaluate_model_definitions(environment.model_definitions)

    # figure
    for _ in range(config['sample_count']):
        new_values = evaluate_model_definitions(environment.model_definitions)
        prior_probability = get_prior_probability(new_values, environment)
        likelihood = get_likelihood(new_values, environment)

        # now: find everywhere the latent variable is used?
        # maybe make some sort of dependency graph
        # check through argument lists for strings, make substitutions
        # need to keep track of values for each step
        pass


