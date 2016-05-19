from __future__ import division
from parser import *
from environment import *
from heron_builtins import *
from util import *

################### Convenience functions

def is_model_definition(line):
    return line[1] == '~'

def is_variable_assignment(line):
    return line[1] == '='

def split_function_application(name_and_args):
    name = name_and_args[0]
    args = name_and_args[1]
    return name, args



################### Evaluation

def evaluate_definition(line, environment):
    variable = line[0]
    name, args = split_function_application(line[2])
    environment.add_variable_definition(variable, name, args)

def evaluate_assignment(line, environment):
    variable = line[0]
    assignment = line[2]
    environment.add_variable_assignment(variable, assignment)


def evaluate_function_application(line, environment):
    function_name = line[0]
    argument = evaluate_expression(line[1])

def evaluate_expression(expression):
    pass

def evaluate(ast):
    if isinstance(ast, str):
        ast = parse(ast)

    environment = Environment()

    for line in ast:
        if is_model_definition(line):
            evaluate_definition(line, environment)
        elif is_variable_assignment(line):
            evaluate_assignment(line, environment)
        else:
            evaluate_function_application(line, environment)


if __name__ == "__main__":
    add = '(+ 3 9.01)'
    model = '''
        x ~ normal(mu, 1)
        y ~ normal(mu2, 1)
        # data = [1, 2, 3, 4, 5]
        # plot(p(mu|x:data))
    '''

    print(evaluate(model))

'''
Each statement is evaluated, and an environment variable is modified to keep track of everything
Need to keep track of:
    Which variables are associated with what data - could just initialize the data to an empty list?
    Relationships in the model
        variables according to which expressions
    What is being predicted

Variables: observable quantities in the model
Parameters: latent parameters

'''