import random

def guessTheNumber():
    # Dar la bienvenida al juego, y preguntar nombre al usuario
    print("¡Bienvenida a GUESS THE NUMBER!")
    print("¿Para iniciar, dime cuál es tu nombre?", end=" ")
    namePlayer = input(": ")
    if namePlayer.strip() == "":
        namePlayer = "Desconocido"
    print(namePlayer + ", escribe un número entero entre 1 y 100: ")
    
    # Inicializar la suposición del usuario
    suposicion_usuario = []

    # Obtener la entrada del usuario y validarla
    entrada_usuario = obtenerEntradaUsuario()

    # Agregar la primera suposición del usuario
    suposicion_usuario.append(entrada_usuario)

    # Generar el número secreto
    numero_secreto = generateSecretNumber()

    while True:
        # Resolver la suposición del jugador
        turno_jugador = resolveNumber(numero_secreto, entrada_usuario)
        printResolve(turno_jugador)

        # Si el jugador adivina el número, termina el juego
        if turno_jugador == True:
            print("¡" + namePlayer + " Correcto! Adivinaste el número secreto ")
            print("Tus intentos fueron: ", end=" ")
            print(suposicion_usuario)
            break

        # Generar una suposición del ordenador basada en la pista dada por el jugador
        entrada_ordenador = numberBasedOnHint(numero_secreto, turno_jugador, suposicion_usuario)
        suposicion_usuario.append(entrada_ordenador)
        print("--Mi turno: ", end=" ")
        print(entrada_ordenador)

        # Resolver la suposición del ordenador
        turno_ordenador = resolveNumber(numero_secreto, entrada_ordenador)
        printResolve(turno_ordenador)

        # Si el ordenador adivina el número, termina el juego
        if turno_ordenador == True:
            print("He ganado!! adiviné el número secreto")
            print("Mis intentos fueron: ", end=" ")
            print(suposicion_usuario)
            break

        # Obtener la próxima entrada del usuario y agregarla a las suposiciones del usuario
        entrada_usuario = obtenerEntradaUsuario()
        suposicion_usuario.append(entrada_usuario)

    # Preguntar al usuario si desea seguir jugando
    new_play = input('¿Quieres seguir jugando? (S/N)').upper()
    if new_play == 'S':
        guessTheNumber()
    else:
        print('Gracias por jugar, ¡Hasta la próxima!')


def generateSecretNumber():
    return random.randint(1, 100)


def numberBasedOnHint(secret_number, hint, user_guesses):
    if hint == 'menor':
        max_guess = max(user_guesses)
        return random.randint(min(secret_number, max_guess + 1), 100)
    elif hint == 'mayor':
        min_guess = min(user_guesses)
        return random.randint(1, max(secret_number, min_guess - 1))


def resolveNumber(numero_correcto, entrada_usuario):
    if entrada_usuario > numero_correcto:
        return "mayor"
    elif entrada_usuario < numero_correcto:
        return "menor"
    elif entrada_usuario == numero_correcto:
        return True


def printResolve(resolve):
    if resolve == "mayor":
        print("Muy alto... El número secreto es menor")
    elif resolve == "menor":
        print("Muy bajo... El número secreto es mayor")


def validateInput(guess_number):
    # si no es un numero entero o la cadena está vacia
    if not guess_number.isdigit() or not guess_number.strip():
        return False
    else:
        return True

def obtenerEntradaUsuario():
    entrada_usuario = input('--> ')
    # Validar la entrada del usuario
    while not validateInput(entrada_usuario):
        print("Por favor, escribe un número válido entre 1 y 100")
        entrada_usuario = input('--> ')
    # Convertir la entrada del usuario a entero
    return int(entrada_usuario)


if __name__ == "__main__":
    guessTheNumber()
