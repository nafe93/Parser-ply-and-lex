import ply.lex as lex

# Имя токенов всегда требуется
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Правила регулярных выражений для токенов
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Правило регулярного выражения с функцией действия

# Что такое число
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t