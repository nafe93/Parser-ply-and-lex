# library
import ply.yacc as yacc
# my file
from calclex import tokens
import calclex


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def tautology_conjunction(p):
    if p[1] == "~" + p[3]:
        p[0] = 0
    if p[3] == "~" + p[1]:
        p[0] = 0


def tautology_disjunction(p):
    if p[1] == "~" + p[3]:
        p[0] = 1
    if p[3] == "~" + p[1]:
        p[0] = 1


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
    buffer = list(p[3])

    if buffer[0] == '(':
        for i, v in enumerate(buffer):
            if buffer[i] == '(' or buffer[i] == ')':
                buffer[i] = ""
            elif buffer[i] == '/':
                buffer[i] == ""
            elif buffer[i] == '\\':
                buffer[i] == ""
            else:
                buffer[i] = "(" + str(p[1]) + "/\\" + v + ")"


        p[0] = "(" + "".join(buffer) + ")"
    else:
        p[0] = p[1] + "/\\" + p[3]


    tautology_conjunction(p)


def p_factor_disjunction(p):
    'expression : expression DISJUNCTION term'
    p[0] = p[1] + "\\/" + p[3]
    tautology_disjunction(p)


def p_factor_implication(p):
    'expression : expression IMPLICATION term'
    p[0] = "~" + p[1] + "\\/" + p[3]


def p_factor_negation(p):
    'factor : NEGATION factor'
    if len(p[2]) == 1:
        p[0] = p[1] + p[2]
    elif len(p[2]) > 1:

        buffer = list(p[2])

        for i, val in enumerate(buffer):
            if val == '(' or val == ')':
                buffer[i] = val
            elif val == '~':
                buffer[i] = '~'
            elif val == '\\':
                buffer[i] = '/'
            elif val == '/':
                buffer[i] = '\\'
            else:
                buffer[i] = "~" + val
        p[0] = ''.join(buffer)


def p_factor_dnegation(p):
    'factor : DNEGATION CHARS'
    p[0] = p[2]


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    if len(p[2]) == 1:
        p[0] = p[2]
    else:
        p[0] = '(' + p[2] + ')'


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
    result = parser.parse(result)
    print(result)