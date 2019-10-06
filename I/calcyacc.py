# library
import ply.yacc as yacc

# my file
from calclex import tokens


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_chars(p):
    'factor : CHARS'
    p[0] = p[1]

def p_factor_conjuction(p):
    'expression  : expression CONJUNCTION term'
    p[0] = p[1] + "/\\" + p[3]


def p_factor_disjunction(p):
    'expression : expression DISJUNCTION term'
    p[0] = p[1] + "\\/" + p[3]


def p_factor_implication(p):
    'expression : expression IMPLICATION term'
    p[0] = "~" + p[1] + "\\/" + p[3]


def p_factor_negation(p):
    'factor : NEGATION factor'
    p[0] = p[1] + p[2]


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Ошибка ввода!")


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