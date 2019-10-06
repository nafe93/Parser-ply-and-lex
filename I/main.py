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
    'CHARS',
    'CONJUNCTION',
    'DISJUNCTION',
    'IMPLICATION',
    'NEGATION'
)

# Правила регулярных выражений для токенов
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CONJUNCTION = r'/\\'
t_DISJUNCTION = r'\\/'
t_IMPLICATION = r'->'


# Правило регулярного выражения с функцией действия
# Что такое число
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Все буквы
def t_CHARS(t):
    r'[A-Za-z]+'
    t.value = str(t.value)
    return t

# Перенос строки
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Вывод ошибки
def t_error(t):
    print(f"В символе под номером : {t.value[0]} произошла ошибка")
    t.lexer.skip(1)

lexer = lex.lex()

data = "pp + v"

lexer.input(data)

while True:
     tok = lexer.token()
     if not tok:
         break      # No more input
     print(tok)