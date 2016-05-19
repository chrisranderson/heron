import numpy as np

class Environment:

    def __init__(self):
        self.variable_definitions = {}
        self.variable_assignments = {}
        self.functions = {}
        self.latent_variables = set()

    # setters
    def add_model_definition(self, var_name, function_name, args):
        self.variable_definitions[var_name] = (function_name, args)

    def add_variable_assignment(self, var_name, expression):
        self.variable_assignments[var_name] = np.asarray(list(expression), float)

    def add_function(self, function):
        self.functions[function.__name__] = function

    def add_latent_variable(self, variable_name):
        self.latent_variables.add(variable_name)

    # getters
    def get_function(self, function_name):
        return self.functions[function_name]

    def get_variable_value(self, var_name):
        return self.variable_assignments[var_name]

