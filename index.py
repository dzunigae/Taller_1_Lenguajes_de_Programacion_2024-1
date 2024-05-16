from ply import lex

# Definición de tokens
tokens = (
    'ID',
    'KEYWORD',
    'INTEGER',
    'FLOAT',
    'STRING',
    'CHARACTER',
    'ARITHMETIC_OPERATOR',
    'RELATIONAL_OPERATOR',
    'ASSIGNMENT_OPERATOR',
    'DELIMITER',
    'CALL'
)

# Expresiones regulares para tokens simples

# Identificadores
#def t_ID(t):
#    r'[a-z_][a-z0-9_]*'
#    return t

# Palabras clave
vocabulario = {
    'mostrar':'MOSTRAR',
    'si':'SI',
    'sino':'SINO',
    'caso':'CASO',
    'mientras':'MIENTRAS',
    'repita':'REPITA',
    'para':'PARA',
    'hasta':'HASTA',
    'funcion':'FUNCION',
    'retornar':'RETORNAR',
    'nada':'NADA',
    'tipo':'TIPO',
    'tamaño':'TAMAÑO',
    'entero':'ENTERO',
    'real':'REAL',
    'arreglo':'ARREGLO',
    'cadena':'CADENA',
    'racha':'RACHA',
    'alfabeto':'ALFABETO',
    'categoria':'CATEGORIA',
    'alfa':'ALFA',
    'tau':'TAU',
    'beta':'BETA',
    'delta':'DELTA',
    'modelo':'MODELO',
    'add':'ADD',
    'posicion':'POSICION',
    'inicio_main':'INICIO',
    'fin_main':'FIN',
    'ordenar_mayor':'O_MAYOR',
    'ordenar_menor':'O_MENOR',
    'multicotomizacion':'MULTICOTOMIZACION',
    'datos_modelo':'DATOS_MODELO',
    'datos_tratamiento':'DATOS_TRATAMIENTO',
    'conjunto_datos':'CONJUNTO_DATOS',
    'conjunto_datos_bloque':'CONJUNTO_DATOS_BLOQUE',
    'conjunto_datos_tratamiento':'CONJUNTO_DATOS_TRATAMIENTO',
    'numero_rachas_hasta_dato':'NUMERO_RACHAS_HASTA_DATO',
    'rachas_celda':'RACHAS_CELDA',
    'promedio_rachas_celda':'PROMEDIO_RACHAS_CELDA',
    'rachas_bloque':'RACHAS_BLOQUE',
    'rachas_tratamiento':'RACHAS_TRATAMIENTO',
    'promedio_rachas_bloque':'PROMEDIO_RACHAS_BLOQUE',
    'promedio_rachas_tratamiento':'PROMEDIO_RACHAS_TRATAMIENTO',
    'rachas_modelo':'RACHAS_MODELO',
    'promedio_rachas_modelo':'PROMEDIO_RACHAS_MODELO',
    'y':'Y',
    'o':'O',
    'div':'DIV',
    'mod':'MOD',
    'no':'NO'
}

#def t_KEYWORD(t):
#    r'\b(?:' + '|'.join(vocabulario.keys()) + r')\b'
#    t.type = vocabulario.get(t.value, 'ID')
#    return t

#Identificadores y palabras reservadas
def t_ID(t):
    r'[a-z_][a-z0-9_]*'
    t.type = 'KEYWORD' if t.value in vocabulario else 'ID'
    return t

# Entero
def t_INTEGER(t):
    r'-?\d+'
    t.value = int(t.value)  # Convertir el valor del token a entero
    return t

# Real
def t_FLOAT(t):
    r'-?\d+\.\d+'  # El signo "-" es opcional
    t.value = float(t.value)  # Convertir el valor del token a flotante
    return t

# Cadena 
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Eliminar comillas del valor del token
    return t

# Caracter
def t_CHARACTER(t):
    r"'[^']'"
    t.value = t.value[1]  # Obtener el caracter sin las comillas
    return t

# Operadores aritméticos
operadores_aritmeticos = {
    '+':'MAS',
    '-':'RESTA',
    '*':'MULTIPLICACION',
    '**':'POTENCIACION',
    '/':'DIVISION',
}

def t_ARITHMETIC_OPERATOR(t):
    r'\+|-|\*|\*\*|/'
    t.type = operadores_aritmeticos.get(t.value)
    return t

# Operadores relacionales
operadores_relacionales = {
    '==':'IGUAL_QUE',
    '<':'MENOR_QUE',
    '>':'MAYOR_QUE',
    '<=':'MENOR_IGUAL_QUE',
    '>=':'MAYOR_IGUAL_QUE',
    '!=':'DISTINTO_QUE'
}

def t_RELATIONAL_OPERATOR(t):
    r'==|<|>|<=|>=|!='
    t.type = operadores_relacionales.get(t.value)
    return t

# Operador de asignación
def t_ASSIGNMENT_OPERATOR(t):
    r'='
    return t

# Delimitadores
def t_DELIMITER(t):
    r'[\(\)\{\}\[\],;]'
    return t

# Llamado de métodos o atributos
def t_CALL(t):
    r'\.'
    return t

# Comentarios
def t_COMMENT(t):
    r'\#\#.*'
    pass  # Ignorar comentarios de una línea

def t_COMMENT_BLOCK(t):
    r'\#.*?\#'
    pass  # Ignorar comentarios de bloque

###################################################################

############# Falta revisar de aquí hacia abajo ###################

###################################################################

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Regla para manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Ejemplo de uso del lexer
if __name__ == "__main__":
    # Datos de entrada
    data = """
    
    entero numero_1 = 11;

    numero.hola

    """

    # Darle entrada al lexer
    lexer.input(data)

    # Iterar sobre los tokens
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
