class UndefinedVariableException(Exception):
    def __init__(self, variable):
        print('The variable "{}" is undefined. Only model definitions can have undefined variables.'.format(variable))