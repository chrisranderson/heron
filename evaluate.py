from __future__ import division
from parser import *
from environment import *
from heron_builtins import *
from util import *
from exceptions import *

################### Convenience functions
def first(array):
    return array[0]

def second(array):
    return array[1]

def evaluate_list(a_list, environment):
    return list(map(lambda list_item: evaluate_expression(list_item, environment), a_list))
################### Evaluation

def evaluate_definition(line, environment):
    ((_, variable_name), (_, (((_, function_name), (_, argument_list))))) = line # wowza
    argument_list = list(map(lambda argument: evaluate_expression(argument, environment, True), argument_list))
    environment.add_model_definition(variable_name, function_name, argument_list)

def evaluate_assignment(line, environment):
    ((_, variable_name), assignment_value) = line
    environment.add_variable_assignment(variable_name, evaluate_expression(assignment_value, environment))

def evaluate_function_application(line, environment):
    ((_, function_name), (_, argument_list)) = line
    function = environment.get_function(function_name)
    argument_list = evaluate_list(argument_list, environment)
    return function(*argument_list)

def evaluate_probability_expression(line, environment):
    (_, (_, latent_variables), (_, (observation_list))) = line
    latent_variables = list(map(second, latent_variables))
    observation_list = list((map(second, observation_list)))

    for latent_variable in latent_variables:
        environment.add_latent_variable(latent_variable)

    for observation in observation_list:
        evaluate_observation(*(map(second, observation)))

def evaluate_observation(variable_name, observations):
    pass

def evaluate_expression(expression, environment, allow_unevaluated=False):
    expression_type, expression_value = expression
    if expression_type == 'variable':
        if allow_unevaluated:
            return expression_value
        else:
            try:
                return environment.get_variable_value(expression_value)
            except KeyError as e:
                raise UndefinedVariableException(expression_value)

    elif expression_type == 'number':
        return string_to_number(expression_value)

    elif expression_type == 'list_literal':
        return evaluate_list(expression_value, environment)

    elif expression_type == 'probability_expression':
        return evaluate_probability_expression(expression_value, environment)


def evaluate(ast):
    if isinstance(ast, str):
        ast = parse(ast)

    environment = initialize_environment(Environment())

    for line in ast:
        line_type, line_value = line
        if line_type == 'model_definition':
            evaluate_definition(line_value, environment)
        elif line_type == 'assignment':
            evaluate_assignment(line_value, environment)
        elif line_type == 'function_application':
            evaluate_function_application(line_value, environment)

if __name__ == "__main__":
    add = '(+ 3 9.01)'
    model = '''
        x ~ normal(mu, 1)
        y ~ normal(mu2, 1)
        data = [1, 2, 3, 4, 5]
        plot(p(mu, mu2|x:data, y:data))
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