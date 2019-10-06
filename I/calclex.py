import sys
import ply.lex as lex

tokens = (
    'NUMBER',
    'CHARS',
    'LPAREN',
    'RPAREN',
    'CONJUNCTION',
    'DISJUNCTION',
    'IMPLICATION',
    'NEGATION',
    'DNEGATION',
    'DDNF',
    'DCNF'
)
# Имя токенов всегда требуется

# Правила регулярных выражений для токенов
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CONJUNCTION = r'/\\'
t_DISJUNCTION = r'\\/'
t_IMPLICATION = r'->'
t_NEGATION = r'~'
t_DNEGATION = r'~~'
t_DDNF = r'[a-zA-z0-9 ]+/\\\([a-zA-z0-9 ]+\\/[a-zA-z0-9 ]+\)'
t_DCNF = r'[a-zA-z0-9 ]+\\/\([a-zA-z0-9 ]+/\\[a-zA-z0-9 ]+\)'


# Правило регулярного выражения с функцией действия
# Что такое число
def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f"Строка {t.lineno}: номер {t.value} очень большая!")
        t.value = 0
    return t


# Все буквы
def t_CHARS(t):
    r'[A-Za-z ]+'
    try:
        t.value = str(t.value)
    except ValueError:
        print(f"Строка {t.lineno}: номер {t.value} есть ошибка!")
        t.value = 0
    return t


# Перенос строки
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# игнор
t_ignore = ' \t'


# Вывод ошибки
def t_error(t):
    print(f"В символе под номером : {t.value[0]} произошла ошибка")
    t.lexer.skip(1)


lexer = lex.lex()

data = "~~p \/ (~p /\ q) -> d"
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
