import random


def obtener_cartas():
    # Definimos dos listas: una para los palos de las cartas
    # y otra para los valores de las cartas.
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
               'J', 'Q', 'K', 'A']

    # Creamos una lista vacía para almacenar las cartas seleccionadas al azar.
    cartas = []

    # Ejecutamos un bucle while hasta que hayamos obtenido 4 cartas distintas.
    while len(cartas) < 4:
        # Seleccionamos un palo al azar de la lista 'palos'.
        palo = random.choice(palos)

        # Seleccionamos un valor al azar de la lista 'valores'.
        valor = random.choice(valores)

        # Creamos una cadena que representa una carta en el formato
        # 'Valor de Palo' (por ejemplo, '5 de Corazones').
        carta = f'{valor} de {palo}'

        # Verificamos si la carta ya ha sido seleccionada anteriormente
        # (para evitar duplicados).
        if carta not in cartas:
            # Si la carta no está en la lista 'cartas', la agregamos.
            cartas.append(carta)

    # Devolvemos la lista de 4 cartas seleccionadas al azar.
    return cartas


# Ejemplo de uso:
mis_cartas = obtener_cartas()
print(mis_cartas)
