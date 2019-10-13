import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calc_lex import MyLexer

tokens = MyLexer().tokens

global_list = list()


# Работа с строками
def negation(my_string):
    if '~' in my_string:
        my_string = my_string[1:]
    else:
        my_string = '~' + my_string

    return my_string


# Проверка на статисфайбл
def resolution(_list, debug=0):
    # first tuple
    for _index_tuple_1, _tuple_1 in enumerate(_list):
        if debug == 1:
            print(_list)
        # second tuple
        for _index_tuple_2, _tuple_2 in enumerate(_list[_index_tuple_1 + 1:]):
            # get element from tuple one
            for index_element_1, a in enumerate(_tuple_1):
                # get element from tuple two
                for index_element_2, b in enumerate(_tuple_2):
                    if a is not None and negation(a) == b:
                        result_1 = _tuple_1[1 - index_element_1]
                        result_2 = _tuple_2[1 - index_element_2]
                        if result_1 is None and result_2 is None:
                            _list.clear()
                            return "not satisfiable"
                        elif result_1 == result_2 and result_1 is not None:
                            _list.append([result_1, None])
                        else:
                            _list.append([result_1, result_2])
    _list.clear()
    return "satisfiable"


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
    _negation = negation(p[1])
    p[0] = _negation + '\\/' + p[3]
    if negation == p[3]:
        global_list.append([None, p[3]])
    else:
        global_list.append([_negation, p[3]])


# Операции над AND
def p_and_exp_exp_operators(p):
    '''expression  : expression AND expression'''
    p[0] = p[1] + '/\\' + p[3]
    if p[1] is not None:
        global_list.append([p[1], None])
    if p[3] is not None:
        global_list.append([p[3], None])


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
    # debug = 1 or 0
    # 1 view how the logic work
    # 0 disable how the logic work
    result = resolution(global_list, debug=0)
    print(result)
