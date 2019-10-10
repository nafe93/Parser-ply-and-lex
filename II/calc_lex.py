# ------------------------------------------------------------
# calc_lex.py
#
# tokenizer for a simple expression evaluator for
# variable has this type of operations => and,or,negation,double negation,de morgan,distributive
# ------------------------------------------------------------
import ply.lex as lex


class MyLexer(object):
    # List of token names
    tokens = (
        'VARIABLE',
        'AND',
        'OR',
        'IMP',
        'LPAREN',
        'RPAREN',
    )

    # Регулярные выражения
    # логические работают с двумя переменными
    t_AND = r'/\\'
    t_OR = r'\\/'
    t_IMP = r'->'
    # Скопки
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    # A regular expression
    def t_VARIABLE(self, t):
        r'~?[A-Za-z]+'
        t.value = str(t.value)
        return t

    # Переход строки
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Игнор тобуляций
    t_ignore = ' \t'

    # Error handling rule
    def t_error(self, t):
        print("Запрешенный знак '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

# Build the lexer and try it out
m = MyLexer()
m.build()           # Build the lexer
# m.test("p/\\((s/\\t)\\/l)")     # Test it
m.test("~p")