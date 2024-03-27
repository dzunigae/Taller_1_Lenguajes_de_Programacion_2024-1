<!--Documento revisado hasta el algoritmo 1-1 Multicotomización del modelo de dos vías-->

# Reglas generales
No existen las mayúsculas en este lenguaje, en caso de haber, se considerarán un error.  
Todas las variables son globales.  

# Datos primitivos soportados
Entero (Incluye - para negativos, no soporta + para positivos)  
Real (Incluye - para negativos, no soporta + para positivos)  
string (Símbolos entre "", son las rachas y cadenas.)  
Char (Símbolos cualquieras, no es necesario que estén entre comillas ni nada, son las categorías.)

# Estructuras de datos soportadas
Arreglos (Supongo que las matrices se pueden manejar como arreglos de arreglos, soportan cualquier tipo de dato, se debe declarar su tamaño, el cual puede ser multidimensional)  
Conjuntos (Podríamos decir que sets)  

# Vocabulario
**//:** Comentario de línea.  
**# #:** Comentario de bloque.  
**mostrar:** Escribir en pantalla.  
**inicio_main:** Inicio de la secuencia principal del programa.  
**fin_main:** Final de la secuencia principal del programa.  
**inicio_funcion:** Inicio del bloque de código que corresponde a una función anteriormente definida.  
**fin_funcion:** Final del bloque de código que corresponde a una función anteriormente definida.  
**entero:** Definición de una variable con un entero.  
**real:** Definición de una variable con un real.  
**racha:** Definición de una racha, la cual sería un string.  
**alfabeto:** Definición de un alfabeto, el cual sería un arreglo.  
**cadena:** Definición de una cadena, la cual sería un string.  
**conjunto:** Definición de un conjunto, el cual sería un set de enteros o reales.  
**categoria:** En sí las letras que componen el alfabeto, son char.  
**alfa:** Definición del parámetro efecto del modelo (Es un real)  
**tau:** Definición del parámetro efectos de los tratamientos (Es un arreglo)  
**beta:** Definición del parámetro efectos de los bloques (Es un arreglo)  
**delta:** Definición de la matriz de los datos del modelo (Es un arreglo multidimensional)  
**bloque:** Definición de lo que sería un bloque de una matriz (Es un arreglo multidimensional)  
**tratamiento:** Definición de lo que sería un tratamiento de una matriz (Es un arreglo multidimensional)  
**si:** Equivalente al if.  
**sino:** Equivalente al else.  
**caso:** Equivalente a switch. 
**mientras:** Equivalente a While.  
**repita:** Equivalente a Do.  
**para:** Equivalente a for.  
**hasta:** Indicador de cual será el final del ciclo "para".  
**funcion:** Forma de declarar una función.  
**retornar:** Valor de retorno de una función.  
**nada:** Palabra especial para poner en el retorno que hace que la función no retorne nada.  
**arreglo:** Definición de una variable que será un arreglo.  
**multicotomizacion:** Función especial de multicotomizacion.  
**contadora:** Función especial contadora de la cadena multicotomizada.  
**datos_modelo:** Función especial que da el total de datos del modelo de dos vías de clasificación.  
**datos_bloque:** Función especial que da el total de datos del bloque.  
**datos_tratamiento:** Función especial que da el total de datos del tratamiento.
**conjunto_datos:** Función especial que da el conjunto de todos de datos del modelo de dos vías de clasificación.  
**conjunto_datos_bloque:** Función especial que da el conjunto de todos los datos del bloque.  
**conjunto_datos_tratamiento:** Función especial que da el conjunto de todos los datos del tratamiento.  
**numero_rachas_hasta_dato:** Función especial que da el número de rachas que se forman hasta la ubicación del dato especificado.  
**rachas_celda:** Función especial que da el número de rachas en la celda especificada.  
**promedio_rachas_celda:** Función especial que da el promedio de rachas en la celda especificada.
**rachas_bloque:** Función especial que da la suma del número de rachas en el bloque especificado.
**rachas_tratamiento:** Función especial que da la suma del número de rachas en el tratamiento especificado.
**promedio_rachas_bloque:** Función especial que da el promedio de rachas en el bloque especificado.
**promedio_rachas_tratamiento:** Función especial que da el promedio de rachas en el tratamiento especificado.
**rachas_modelo:** Función especial que da la suma del número de rachas de todo el modelo.
**promedio_rachas_modelo:** Función especial que da el promedio del número de rachas de todo el modelo.

# Operaciones
**=:** Asignación  
**+:** Suma  
**-:** Resta  
***:** Multiplicación  
**/:** División  
**div:** División entera  
**mod:** Operador módulo  
**():** Agrupación de expresiones  
**y:** "y" lógico  
**o:** "o" lógico  
**==:** Operador igual que  
**<:** Operador menor que  
**>:** Operador mayor que  
**<=:** Operador menor que  
**>=:** Operador mayor que  
**!=:** Operador distinto que  