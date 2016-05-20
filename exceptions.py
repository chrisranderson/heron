# TODO: you used the variable "dara", did you mean "data"? If yes, continue execution, and swap variable out.
class UndefinedVariableException(Exception):
    def __init__(self, variable):
        print('The variable "{}" is undefined. Only model definitions can have undefined variables.'.format(variable))

class UndefinedFunctionException(Exception):
    def __init__(self, function_name):
        print('The function "{}" is undefined.'.format(function_name))

class ImproperPriorException(Exception):
    def __init__(self, variable_name):
        print('The latent variable {} does not have a defined prior.'.format(variable_name))