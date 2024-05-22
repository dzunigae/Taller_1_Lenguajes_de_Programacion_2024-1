import ply.lex as lex
import re

# Definición de tokens
tokens = (
    'ID',
    'KEYWORD',
    'INTEGER',
    'FLOAT',
    'STRING',
    'CHARACTER',
    'MAS',  # +
    'RESTA',  # -
    'MULTIPLICACION',  # *
    'POTENCIACION',  # **
    'DIVISION',  # /
    'IGUAL_QUE',  # ==
    'MENOR_QUE',  # <
    'MAYOR_QUE',  # >
    'MENOR_IGUAL_QUE',  # <=
    'MAYOR_IGUAL_QUE',  # >=
    'DISTINTO_QUE',  # !=
    'ASSIGNMENT_OPERATOR',  # =
    'COLON',  # :
    'DELIMITER',
    'CALL'
)

# Expresiones regulares para tokens simples

# Identificadores y palabras reservadas
vocabulario = {
    'mostrar': 'MOSTRAR',
    'si': 'SI',
    'sino': 'SINO',
    'caso': 'CASO',
    'mientras': 'MIENTRAS',
    'repita': 'REPITA',
    'para': 'PARA',
    'hasta': 'HASTA',
    'funcion': 'FUNCION',
    'retornar': 'RETORNAR',
    'nada': 'NADA',
    'tipo': 'TIPO',
    'tamaño': 'TAMAÑO',
    'entero': 'ENTERO',
    'real': 'REAL',
    'arreglo': 'ARREGLO',
    'cadena': 'CADENA',
    'racha': 'RACHA',
    'alfabeto': 'ALFABETO',
    'categoria': 'CATEGORIA',
    'alfa': 'ALFA',
    'tau': 'TAU',
    'beta': 'BETA',
    'delta': 'DELTA',
    'modelo': 'MODELO',
    'add': 'ADD',
    'posicion': 'POSICION',
    'inicio_main': 'INICIO',
    'fin_main': 'FIN',
    'ordenar_mayor': 'O_MAYOR',
    'ordenar_menor': 'O_MENOR',
    'multicotomizacion': 'MULTICOTOMIZACION',
    'datos_modelo': 'DATOS_MODELO',
    'datos_tratamiento': 'DATOS_TRATAMIENTO',
    'conjunto_datos': 'CONJUNTO_DATOS',
    'conjunto_datos_bloque': 'CONJUNTO_DATOS_BLOQUE',
    'conjunto_datos_tratamiento': 'CONJUNTO_DATOS_TRATAMIENTO',
    'numero_rachas_hasta_dato': 'NUMERO_RACHAS_HASTA_DATO',
    'rachas_celda': 'RACHAS_CELDA',
    'promedio_rachas_celda': 'PROMEDIO_RACHAS_CELDA',
    'rachas_bloque': 'RACHAS_BLOQUE',
    'rachas_tratamiento': 'RACHAS_TRATAMIENTO',
    'promedio_rachas_bloque': 'PROMEDIO_RACHAS_BLOQUE',
    'promedio_rachas_tratamiento': 'PROMEDIO_RACHAS_TRATAMIENTO',
    'rachas_modelo': 'RACHAS_MODELO',
    'promedio_rachas_modelo': 'PROMEDIO_RACHAS_MODELO',
    'y': 'Y',
    'o': 'O',
    'div': 'DIV',
    'mod': 'MOD',
    'no': 'NO'
}

# Modificar la expresión regular para incluir caracteres Unicode
def t_ID(t):
    r'[a-zñ_][a-z0-9ñ_]*'
    t.type = 'KEYWORD' if t.value in vocabulario else 'ID'
    return t

# Mover FLOAT antes de INTEGER
# Real
def t_FLOAT(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

# Entero
def t_INTEGER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

# Cadena
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

# Caracter
def t_CHARACTER(t):
    r"'[^']'"
    t.value = t.value[1]
    return t

# Operadores aritméticos
def t_MAS(t):
    r'\+'
    return t

def t_RESTA(t):
    r'-'
    return t

def t_MULTIPLICACION(t):
    r'\*'
    return t

def t_POTENCIACION(t):
    r'\*\*'
    return t

def t_DIVISION(t):
    r'/'
    return t

# Operadores relacionales
def t_MENOR_IGUAL_QUE(t):
    r'<='
    return t

def t_MAYOR_IGUAL_QUE(t):
    r'>='
    return t

def t_DISTINTO_QUE(t):
    r'!='
    return t

def t_IGUAL_QUE(t):
    r'=='
    return t

def t_MENOR_QUE(t):
    r'<'
    return t

def t_MAYOR_QUE(t):
    r'>'
    return t

# Operador de asignación
def t_ASSIGNMENT_OPERATOR(t):
    r'='
    return t

# Operador de dos puntos
def t_COLON(t):
    r':'
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
    pass

def t_COMMENT_BLOCK(t):
    r'\#[\s\S]*?\#'
    pass

# Ignorar espacios y tabulaciones
t_ignore = ' \t\n'

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

    """

    # Darle entrada al lexer
    lexer.input(data)

    # Iterar sobre los tokens
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

