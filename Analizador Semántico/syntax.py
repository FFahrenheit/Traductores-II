from ply import lex, yacc

errors = []
symbol_table = {}

'''
    Tokens and rules for lexical analyzer 
'''
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
    global errors
    errors.append(f"[Línea {t.lineno}] Error léxico: Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Newline rule (track line number)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Precedence rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

'''
    Syntax analyzer rules 
'''
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
    # Check if variable is already defined
    if p[1] in symbol_table:
        errors.append(f"[Línea {p.lineno(1)}] Error semántico: Variable '{p[1]}' ya está definida")
        return 
    symbol_table[p[1]] = p[3]
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
    global errors
    # Check if variable is not defined
    if p[1] not in symbol_table:
        errors.append(f"[Línea {p.lineno(1)}] Error semántico: Variable '{p[1]}' no está definida")
        return
    p[0] = ('identifier', p[1])

# Syntax error handler
def p_error(p):
    global errors
    if p:
        errors.append(f"[Línea {p.lineno}] Error de sintaxis en '{p.value}'")
    else:
        errors.append("Error de sintaxis al final de la entrada")

# Export function to parse input
def parse_input(input_string):
    # Lexical analyzer
    lexer = lex.lex()
    # Syntax analyzer
    parser = yacc.yacc()
    global errors, symbol_table
    symbol_table = {}
    errors.clear()
    return parser.parse(input_string)

# Export function to get errors during analysis
def get_errors():
    global errors
    return errors