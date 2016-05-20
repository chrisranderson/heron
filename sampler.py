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

def generate_samples(environment):
    old_values = evaluate_model_definitions(environment.model_definitions)

    # figure
    for _ in range(config['sample_count']):
        new_values = evaluate_model_definitions(environment.model_definitions)

        old_value = computed_values['mu']
        new_value

        latent_variable = environment.latent_variables[0]
        distribution, arguments = environment.get_model_definition(latent_variable)
        proposal = distribution(*arguments)

        # now: find everywhere the latent variable is used?
        # maybe make some sort of dependency graph
        # check through argument lists for strings, make substitutions
        # need to keep track of values for each step
        pass


