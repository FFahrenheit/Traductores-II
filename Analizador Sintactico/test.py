from ply import lex, yacc

errors = []

# Definición de tokens
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

# Expresiones regulares para tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_SEMICOLON = r';'

t_ignore = ' \t'

# Regla para el token de identificador
def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    return t

# Regla para el token de número
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Manejo de errores léxicos
def t_error(t):
    global errors
    errors.append(f"Error léxico en línea {t.lineno}: Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Regla para rastrear el número de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Construcción del analizador léxico
lexer = lex.lex()

# Reglas de precedencia
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Regla de la gramática para la asignación
def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS expression SEMICOLON'''
    p[0] = ('assignment', p[1], p[3])

# Regla de la gramática para el programa
def p_program(p):
    '''program : assignment
               | assignment program'''
    if len(p) == 2:
        p[0] = ('program', p[1])
    else:
        p[0] = ('program', p[1], p[2])

# Regla de la gramática para las expresiones
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

# Manejo de errores sintácticos
def p_error(p):
    if p:
        errors.append(f"Error sintáctico en línea {p.lineno}: '{p.value}'")
    else:
        errors.append("Error sintáctico: EOF inesperado")

# Construcción del analizador sintáctico
parser = yacc.yacc()

# Función para analizar la entrada
def parse_input(input_string):
    global errors
    errors.clear()
    return parser.parse(input_string)

if __name__ == "__main__":
    while True:
        try:
            lexer = lex.lex()
            parser = yacc.yacc()
            s = input('Ingrese la sentencia a analizar: ')
            s = 'x=1+2;\ny=1+2;\nx=3+2;\n'
        except EOFError:
            break
        if not s:
            continue
        result = parse_input(s)
        print(result)
        print(errors)
