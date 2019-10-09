import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calc_lex import MyLexer

tokens = MyLexer().tokens


# Переменные
def p_expr_variable(p):
    'expression : VARIABLE'
    p[0] = p[1]


def p_factor_expr(p):
    '''factor : LPAREN expression RPAREN'''
    p[0] = p[1] + p[2] + p[3]


# Операции над AND
def p_and_exp_exp_operators(p):
    '''expression  : expression AND expression'''
    p[0] = p[1] + '/\\' + p[3]


def p_and_exp_factor_operators(p):
    '''expression  : expression AND factor'''
    variable = p[1]
    factor = list(p[3])

    if factor[0] == '(':
        for i, v in enumerate(factor):
            if factor[i] == '(' or factor[i] == ')':
                factor[i] = ""
            elif factor[i] == '/':
                factor[i] == ""
            elif factor[i] == '\\':
                factor[i] == ""
            else:
                factor[i] = "(" + str(p[1]) + "/\\" + v + ")"
        p[0] = "(" + "".join(factor) + ")"
    else:
        p[0] = p[1] + "/\\" + p[3]




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
    p[0] = '~' + p[1] + '\\/' + p[3]


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
    p[0] = p[1] + '\\/' + p[3]


# Отрицание
def p_negation_exp_operators(p):
    '''expression  : NEGATION expression'''
    p[0] = p[1] + p[2]


def p_negation_factor_operators(p):
    '''expression  : NEGATION factor'''
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
    print(result)
