# Tarea 1, Microprocesadores y Microcontroladores.
# Realizado por:
#   Emiliano Murillo Villalobos - 2018109598
#   Gustavo Enrique Varela Sojo - 2018027232

#################################################################
# Funciones.

# Primer Método. "separa_letras"

# Entradas y Salidas:

# Esta función recibe como entrada el parámetro "cadena",
# el cual se espera que sea un string, compuesto solamente por letras del
# abecedario.
# Esta función devuelve tres valores: un código de error o éxito
# (códigos negativos representan errores y 0 representa éxito),
# la cadena de mayúsculas y la cadena de minúsculas.

def separa_letras(Cadena):
    # Verifica que el parámetro Cadena sea un string.
    if not isinstance(Cadena, str):
        return -100, None, None  # Código de error -100: No es un string.

    # Verifica que el parámetro cadena no sea un string vacío.
    if not Cadena.strip():
        return -300, None, None  # Código de error -300: String vacío.

    # Verifica que el parámetro cadena solo contenga letras del abecedario.
    if not Cadena.isalpha():
        return -200, None, None  # Código de error -200: Contiene caracteres
# que no son letras.

    # Separa el string en dos variables: mayúsculas y minúsculas.
    mayusculas = ''.join(c for c in Cadena if c.isupper())
    minusculas = ''.join(c for c in Cadena if c.islower())

    return 0, mayusculas, minusculas  # Código de éxito 0, y las cadenas de
# mayúsculas y minúsculas.


# Segundo Método. "potencia_manual"

# Entradas y Salidas:

# Esta función recibe dos parámetros, base y potencia, los cuales
# se espera que sean números enteros.
# Esta función devuelve como salidas el resultado de la operación
# base**potencia, sin embargo debe de llegar a ese resultado utilizando
# unicamente sumas y ciclos for.

def potencia_manual(base, potencia):
    # Verifica que los parámetros de entrada no sean de tipo string.
    if isinstance(base, str) or isinstance(potencia, str):
        return -400, None  # Código de error -400: Parámetros de tipo string.

    # Inicializar datos.
    resultado_pot = 1  # Variables que se van a sumar entre ellas para
    resultado_bas = 0  # imitar la operación de cálculo de potencias.
    suma = 0
    base_orig = base

    # Verifica casos especiales: potencia cero y base cero.
    if potencia == 0:
        return 0, resultado_pot  # Código de éxito 0, el resultado es 1.

    if base == 0:
        return 0, resultado_bas  # Código de éxito 0, el resultado es 0.

    # Calcula la potencia mediante un ciclo for.

    # El ciclo for de la variable "i" se ejecuta las veces que pida el
    # parámetro "potencia", mientras que el ciclo for de la variable "j"
    # va a efectuarse según el valor del parámetro "base".

    # La lógica de estos ciclos for consiste en sumar "base" veces el
    # valor de base, guardando el valor en la variable suma, para luego
    # actualizar "base" y repetir.

    # Ejemplo:
    # 7**3: base = 7, suma = 7+7+7+7+7+7+7 = 49.
    # base = suma = 49.
    # base = 49, suma = 49+49+49+49+49+49+49 = 343, que es el resultado
    # buscado.

    abs_potencia = abs(potencia)  # Asegura trabajar con potencias positivas.
    for i in range(abs_potencia-1):  # i va de 0 a potencia-1.
        for j in range(base_orig):  # j va de 0 a base.
            suma += base
        base = suma
        resultado = base
        suma = 0

    # Aplica el inverso si la potencia es negativa.
    if potencia < 0:
        resultado = 1 / resultado

    return 0, resultado  # Código de éxito 0, y el resultado de la operación.

#################################################################

# Programa Principal.
# Cadena = "Prueba"
# print(separa_letras(Cadena))

# base = 3
# potencia = 4
# print(potencia_manual(3, 4))
