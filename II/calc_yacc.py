import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calc_lex import MyLexer

tokens = MyLexer().tokens


# просты булевые операции

def p_and_operators(p):
    p[0] = p[1] + '/\\' + p[3]
    return p[0]


def p_or_operators(p):
    p[0] = p[1] + '\\/' + p[3]
    return p[0]


def p_imp_operator(p):
    p[0] = '~' + p[1] + '\\/' + p[3]
    return p[0]


# Алгоиритмы отрицания, двойного отрицания и де моргана


def p_negation_operators(p):
    p[0] = p[1] + p[2]
    return p[0]


def p_double_negation_operators(p):
    p[0] = p[2]
    return p[0]


# Алгоритмы диструбутивнасти

# def p_dnf_operators(p):
#     p[0] = p[1]
#     return p[0]
#
#
# def p_cnf_operators(p):
#     p[0] = p[1]
#     return p[0]


def p_binary_operators(p):
    '''expression : expression AND term
                  | expression OR term
                  | expression imp term

    term          : term DNF factor
                  | term CNF factor

    factor        : NEGATION factor
                  | DOUBLE_NEGATION factor'''

    # boolean simple
    if p[2] == '/\\':
        p_and_operators(p)
    elif p[2] == '\\/':
        p_or_operators(p)
    elif p[2] == '->':
        p_imp_operator(p)

    # distributive for cnf and dnf
    elif p[2] == '/\\\(' or p[2] == '\)/\\' or p[2] == '\)/\\\(':
        print("test")
    elif p[2] == '\\/\(' or p[2] == '\)\\/' or p[2] == '\)\\/\(':
        print("test")

    # de morgan and negation
    elif p[1] == '~':
        p_negation_operators(p)
    elif p[1] == '~~':
        p_double_negation_operators(p)


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_variable(p):
    'factor : VARIABLE'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[1]


# Error rule for syntax errors
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
