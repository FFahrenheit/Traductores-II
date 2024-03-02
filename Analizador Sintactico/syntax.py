from ply import lex, yacc

errors = []

# Tokens
tokens = (
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'SEMICOLON'
)

# Regex for tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_ignore = ' \t'

# Identifier rule
def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    return t

# Number rule
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Lexical error handler
def t_error(t):
    errors.append(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Regla para rastrear el número de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Lexical analyzer
lexer = lex.lex()

# Precedence rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)
# Program rules
def p_program(p):
    '''program : assignment
               | assignment program'''
    if len(p) == 2:
        p[0] = ('program', p[1])
    else:
        p[0] = ('program', p[1], p[2])

# Assignment rule
def p_assignment(p):
    'assignment : IDENTIFIER EQUALS expression SEMICOLON'
    p[0] = ('assignment', p[1], p[3])

# Expression rule 
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ('identifier', p[1])

# Syntax error hanlder
def p_error(p):
    if p:
        errors.append(f"Sintaxis error en '{p.value}' en la línea {p.lineno}")
    else:
        errors.append("Error de sintaxis al final de la entrada")

# Syntax analyzer
parser = yacc.yacc()

# Función para analizar la entrada
def parse_input(input_string):
    global errors
    errors.clear()
    return parser.parse(input_string)

def get_errors():
    global errors
    return errors