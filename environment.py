import numpy as np

class Environment:

    def __init__(self):
        self.variable_definitions = {}
        self.variable_assignments = {}
        self.functions = {}

    def add_variable_definition(self, var_name, name, args):
        self.variable_definitions[var_name] = (name, args)

    def add_variable_assignment(self, var_name, expression):
        self.variable_assignments[var_name] = np.asarray(list(expression), float)

    def add_function(self, function):
        self.functions[function.__name__] = function

    def get_function(self, function_name):
        return self.functions[function_name]

