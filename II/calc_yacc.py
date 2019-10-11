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


# Проверка на статисфайбл
def is_satisfiable(debug=0):
    if debug == 1:
        print(global_list)
    # First tuple
    for index_tuple, _tuple in enumerate(global_list):
        for index_tuple_list, _tuple_list in enumerate(_tuple):
            buffer = list()
            anti_buffer = list()
            if _tuple_list is not None and '~' in _tuple_list:
                # Second tuple
                for index_second_tuple, second_tuple in enumerate(global_list):
                    for index_second_tuple_list, second_tuple_list in enumerate(second_tuple):
                        # Add all same elements
                        if second_tuple_list is not None and _tuple_list is not None:
                            if _tuple_list == second_tuple_list:
                                buffer.append([index_second_tuple, index_second_tuple_list])
                            if _tuple_list == '~' + second_tuple_list:
                                anti_buffer.append([index_second_tuple, index_second_tuple_list])
                # Second tuple
                for index_second_tuple, second_tuple in enumerate(global_list):
                    for index_second_tuple_list, second_tuple_list in enumerate(second_tuple):
                        # Delete all same elements
                        if second_tuple_list is not None and _tuple_list is not None:
                            if _tuple_list == '~' + second_tuple_list:
                                # _tuple[index_tuple_list] = None
                                # second_tuple[index_second_tuple_list] = None
                                for local_tuple in buffer:
                                    first = local_tuple[0]
                                    second = local_tuple[1]
                                    global_list[first][second] = None
                                for local_tuple in anti_buffer:
                                    first = local_tuple[0]
                                    second = local_tuple[1]
                                    global_list[first][second] = None
                                if debug == 1:
                                    print(global_list)


# Проверить что все элементы None
def all_is_none():
    count = 0
    for index_tuple, _tuple in enumerate(global_list):
        if _tuple == [None, None]:
            print("not satisfiable")
            break

    else:
        print("satisfiable")

    global_list.clear()


# parser logic

# Переменные
def p_expr_variable(p):
    'expression : VARIABLE'
    p[0] = p[1]


def p_factor_expr(p):
    '''factor : LPAREN expression RPAREN '''
    p[0] = p[2]


def p_expr_factor(p):
    'expression : factor'
    p[0] = p[1]


# Операции над imp
def p_imp_exp_exp_operators(p):
    '''expression  : expression IMP expression'''
    negation = parsing_string_for_parsing_string(p[1])
    p[0] = negation + '\\/' + p[3]
    if negation == p[3]:
        global_list.append([None, p[3]])
    else:
        global_list.append([negation, p[3]])


# Операции над AND
def p_and_exp_exp_operators(p):
    '''expression  : expression AND expression'''
    p[0] = p[1] + '/\\' + p[3]
    if '/\\' not in p[1] and '\\/' not in p[1]:
        global_list.append([p[1], None])
    if '/\\' not in p[3] and '\\/' not in p[3]:
        global_list.append([p[3], None])


# Операции над двойным отрицанием
def p_or_exp_exp_operators(p):
    '''expression  : expression OR expression'''
    p[0] = p[1] + '\\/' + p[3]
    if p[1] == p[3]:
        global_list.append([p[1], None])
    else:
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
    # debug = 1 or 0
    # 1 view how the logic work
    # 0 disable how the logic work
    is_satisfiable(debug=0)
    all_is_none()
