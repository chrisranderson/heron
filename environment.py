import numpy as np
from exceptions import *
class Environment:

    def __init__(self):
        self.model_definitions = {}
        self.model_observations = {}

        self.variable_assignments = {}
        self.functions = {}
        self.latent_variables = []

        self.parent_to_children_dependencies = {}
        self.child_to_parent_dependencies = {}

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

    # getters ##########################################################################################################
    def get_function(self, function_name):
        try:
            return self.functions[function_name]
        except:
            raise

    def get_variable_value(self, variable_name):
        return self.variable_assignments[variable_name]

    def get_model_definition(self, variable_name):
        try:
            function, arguments = self.model_definitions[variable_name]
            return function, list(arguments)
        except:
            raise(MissingPriorException(variable_name))

    def get_model_observation(self, variable_name):
        return self.model_observations[variable_name]


    # business #########################################################################################################

    def add_dependency_graph(self):
        for variable_name, (function, arguments) in self.model_definitions.items():
            dependencies = [x for x in arguments if isinstance(x, str)]
            self.parent_to_children_dependencies[variable_name] = dependencies

            for dependent in dependencies:
                if dependent in self.child_to_parent_dependencies:
                    parents = self.child_to_parent_dependencies[dependent]
                    parents.append(variable_name)
                else:
                    self.child_to_parent_dependencies[dependent] = [variable_name]




