import numpy as np
from exceptions import *
class Environment:

    def __init__(self):
        self.model_definitions = {}
        self.model_observations = {}

        self.variable_assignments = {}
        self.functions = {}
        self.latent_variables = []

    # setters
    def add_model_observation(self, variable_name, observations):
        self.model_observations[variable_name] = observations

    def add_model_definition(self, variable_name, function_name, args):
        self.model_definitions[variable_name] = (function_name, args)

    def add_variable_assignment(self, variable_name, expression):
        self.variable_assignments[variable_name] = np.asarray(list(expression), float)

    def add_function(self, function):
        self.functions[function.__name__] = function

    def add_latent_variable(self, variable_name):
        self.latent_variables.append(variable_name)

    # getters
    def get_function(self, function_name):
        try:
            return self.functions[function_name]
        except:
            raise

    def get_variable_value(self, variable_name):
        return self.variable_assignments[variable_name]

    def get_model_definition(self, variable_name):
        try:
            return self.model_definitions[variable_name]
        except:
            raise(ImproperPriorException(variable_name))



