import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calc_lex import MyLexer

tokens = MyLexer().tokens

global_list = list()


# Работа с строками
def parsing_string_for_parsing_string(my_string):
    if '~' in my_string:
        my_string = my_string[1:]
    else:
        my_string = '~' + my_string

    return my_string


# parser logic

# Переменные
def p_expr_variable(p):
    'expression : VARIABLE'
    p[0] = p[1]


def p_factor_expr(p):
    '''factor : LPAREN expression RPAREN'''
    p[0] = p[1] + p[2] + p[3]


# Операции над imp
def p_imp_exp_exp_operators(p):
    '''expression  : expression IMP expression'''
    negation = parsing_string_for_parsing_string(p[1])
    p[0] = negation + '\\/' + p[3]
    global_list.append([negation, p[3]])


def p_predicate_expr(p):
    '''predicate : LPAREN expression RPAREN'''
    p[0] = p[2]


# Операции над AND
def p_and_exp_exp_operators(p):
    '''expression  : expression AND expression'''
    p[0] = p[1] + '/\\' + p[3]
    if len(p[1]) < 3:
        global_list.append([p[1], None])
    if len(p[3]) < 3:
        global_list.append([p[3], None])



def p_and_exp_factor_operators(p):
    '''expression  : expression AND factor'''
    p[0] = p[1] + '/\\' + p[3]
    if len(p[1]) < 3:
        global_list.append([p[1], None])


def p_and_factor_exp_operators(p):
    '''expression  : factor AND expression'''
    p[0] = p[1] + '/\\' + p[3]
    if len(p[3]) < 3:
        global_list.append([None, p[3]])


def p_and_factor_factor_operators(p):
    '''expression  : factor AND factor'''
    p[0] = p[1] + '/\\' + p[3]



# Операции над двойным отрицанием
def p_or_exp_exp_operators(p):
    '''expression  : expression OR expression'''
    p[0] = p[1] + '\\/' + p[3]
    global_list.append([p[1], p[3]])


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
    # print(result)
    # print(global_list)

    for index_tuple, _tuple in enumerate(global_list):
        # First tuple
        for index_tuple_list, _tuple_list in enumerate(_tuple):
            if _tuple_list is not None and '~' in _tuple_list:
                # Second tuple
                for index_second_tuple, second_tuple in enumerate(global_list):
                    for index_second_tuple_list, second_tuple_list in enumerate(second_tuple):
                        if second_tuple_list is not None and _tuple_list is not None:
                            if _tuple_list == '~' + second_tuple_list:
                                _tuple_list = None
                                second_tuple_list = None
                                _tuple[index_tuple_list] = None
                                second_tuple[index_second_tuple_list] = None
                                print(global_list)
