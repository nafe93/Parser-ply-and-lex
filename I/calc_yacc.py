import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calc_lex import MyLexer

tokens = MyLexer().tokens

global_list = list()


# parser logic

# Переменные
def p_expr_variable(p):
    'expression : VARIABLE'
    p[0] = p[1]


def p_factor_expr(p):
    '''factor : LPAREN expression RPAREN'''
    p[0] = p[1] + p[2] + p[3]

    if p[0] not in global_list:
        global_list.append(p[0])

def p_predicate_expr(p):
    '''predicate : LPAREN expression RPAREN'''
    p[0] = p[2]


# Операции над AND
def p_and_exp_exp_operators(p):
    '''expression  : expression AND expression'''
    p[0] = p[1] + '/\\' + p[3]


def p_and_exp_factor_operators(p):
    '''expression  : expression AND factor'''

    variable = p[1]

    element = p[2]

    factor = list(p[3])

    if len(global_list) == 1:
        str = ''.join(global_list)
        if element not in str:

            for i, v in enumerate(factor):

                if factor[i] == '(' or factor[i] == ')':
                    factor[i] = ""
                elif factor[i] == '/':
                    factor[i] == ""
                elif factor[i] == '\\':
                    factor[i] == ""
                else:
                    factor[i] = "(" + variable + "/\\" + v + ")"
            factor_str = ''.join(factor)
            p[0] = factor_str

        else:
            p[0] = p[1] + "/\\" + p[3]
    else:
        for i, v in enumerate(global_list):
            print(v)

        p[0] = p[1] + "/\\" + p[3]
    global_list.clear()

def p_and_factor_exp_operators(p):
    '''expression  : factor AND expression'''
    p[0] = p[1] + '/\\' + p[3]


def p_and_factor_factor_operators(p):
    '''expression  : factor AND factor'''
    p[0] = p[1] + '/\\' + p[3]


# Операции над OR
def p_or_exp_exp_operators(p):
    '''expression  : expression OR expression'''
    p[0] = p[1] + '\\/' + p[3]


def p_or_exp_factor_operators(p):
    '''expression  : expression OR factor'''
    p[0] = p[1] + '\\/' + p[3]


def p_or_factor_exp_operators(p):
    '''expression  : factor OR expression'''
    p[0] = p[1] + '\\/' + p[3]


def p_or_factor_factor_operators(p):
    '''expression  : factor OR factor'''
    p[0] = p[1] + '\\/' + p[3]


# Операции над imp
def p_imp_exp_exp_operators(p):
    '''expression  : expression IMP expression'''
    p[0] = '~' + p[1] + '\\/' + p[3]


def p_imp_exp_factor_operators(p):
    '''expression  : expression IMP factor'''
    p[0] = '~' + p[1] + '\\/' + p[3]


def p_imp_factor_exp_operators(p):
    '''expression  : factor IMP expression'''
    p[0] = '~' + p[1] + '\\/' + p[3]


def p_imp_factor_factor_operators(p):
    '''expression  : factor IMP factor'''
    p[0] = '~' + p[1] + '\\/' + p[3]


# Отрицание
def p_negation_exp_operators(p):
    '''expression  : NEGATION expression'''
    p[0] = p[1] + p[2]


def p_negation_factor_operators(p):
    '''expression  : NEGATION predicate'''
    factor = list(p[2])
    for i, val in enumerate(factor):
        if val == '(' or val == ')':
            factor[i] = val
        elif val == '~':
            factor[i] = '~'
        elif val == '\\':
            factor[i] = '/'
        elif val == '/':
            factor[i] = '\\'
        else:
            factor[i] = "~" + val
    p[0] = ''.join(factor)



def p_double_negation_exp_operators(p):
    '''expression  : DOUBLE_NEGATION expression'''
    p[0] = p[2]


def p_double_negation_factor_operators(p):
    '''expression  : DOUBLE_NEGATION factor'''
    p[0] = p[2]


# Синтаксическая ошибка
def p_error(p):
    print("Синтаксическая ошибка в воде данных!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    result = parser.parse(result)
    print(result)
