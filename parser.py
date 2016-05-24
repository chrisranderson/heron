from pyparsing import *
from util import *
from pprint import pprint

DefinedLater = Forward

def wrap_with_name(name, apply_before=lambda x: x):

    def inner(string, start_position, tokens):
        tokens = apply_before(tokens)[0]
        return (name, tokens)

    return inner

def parse(input_string):
    ParserElement.setDefaultWhitespaceChars([' ', '\t', '   '])

    EXPRESSION = DefinedLater()
    FUNCTION_APPLICATION = DefinedLater()
    PROBABILITY_EXPRESSION = DefinedLater()

    id_regex = Regex('[-a-zA-Z!?_/*+][a-z0-9A-Z!?_/*-]*')
    number_regex = Regex('-?(([0-9]+)|([0-9]*\.[0-9]+))')

    #################### terminals
    l_paren = Literal('(').suppress()
    r_paren = Literal(')').suppress()
    l_bracket = Literal('[').suppress()
    r_bracket = Literal(']').suppress()

    pipe = Literal('|').suppress()
    colon = Literal(':').suppress()
    tilda = Literal('~').suppress()
    equals = Literal('=').suppress()

    newline = Literal('\n').suppress()
    line = OneOrMore('\n').suppress()
    space = Literal(' ').suppress()
    comma = Literal(',').suppress()

    comment = Group('#' + SkipTo(newline)).suppress()

    function_name = id_regex.setParseAction(wrap_with_name('function_name'))
    number = number_regex.setParseAction(wrap_with_name('number'))
    identifier = id_regex.setParseAction(wrap_with_name('identifier'))
    random_variable = id_regex.setParseAction(wrap_with_name('random_variable'))
    variable = id_regex.setParseAction(wrap_with_name('variable'))

    #################### non-terminals
    SPACE_SEPARATED_LIST = DefinedLater()
    SPACE_SEPARATED_LIST.setDefaultWhitespaceChars([])
    SPACE_SEPARATED_LIST = OneOrMore((EXPRESSION + Optional(Or([newline, space, comma]))))

    LIST_LITERAL = Group(l_bracket + SPACE_SEPARATED_LIST + r_bracket).setParseAction(wrap_with_name('list_literal'))
    EXPRESSION << Or([FUNCTION_APPLICATION, LIST_LITERAL, PROBABILITY_EXPRESSION, number, identifier])
    ASSIGNMENT = Group(variable + equals + EXPRESSION).setParseAction(wrap_with_name('assignment'))

    # functions
    ARGUMENT_LIST = Group(SPACE_SEPARATED_LIST).setParseAction(wrap_with_name('argument_list'))
    FUNCTION_APPLICATION << Group(function_name + l_paren + ARGUMENT_LIST + r_paren)\
                                 .setParseAction(wrap_with_name('function_application'))

    # model definition
    OBSERVATION = Group(identifier + colon + EXPRESSION).setParseAction(wrap_with_name('observation'))
    OBSERVATION_LIST = Group(delimitedList(OBSERVATION)).setParseAction(wrap_with_name('observation_list'))
    PROBABILITY_EXPRESSION << Group('p' + l_paren + Group(delimitedList(identifier)).setParseAction(wrap_with_name('latent_variables')) +
                                    Optional(pipe + OBSERVATION_LIST) + r_paren)\
                                    .setParseAction(wrap_with_name('probability_expression'))
    MODEL_DEFINITION = Group(random_variable + tilda + EXPRESSION)\
                            .setParseAction(wrap_with_name('model_definition'))

    STATEMENT = Optional(newline) + Or([MODEL_DEFINITION, ASSIGNMENT, FUNCTION_APPLICATION]) + Optional(newline)
    PROGRAM = OneOrMore(Or([STATEMENT, line, comment]))
    ast = PROGRAM.parseString(input_string)
    return ast

if __name__ == "__main__":
    add = '(+ 3 9.01)'
    model = '''
        x ~ normal(mu ,1)
        y ~ normal(mu2 1)
        data = [1 2 3 4 5]
        plot(
        p(mu|x:data)
        )
    '''

    parsed = parse(model)
    print(parsed)
