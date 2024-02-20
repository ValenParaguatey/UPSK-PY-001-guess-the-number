import random

def numero_aleatorio():
    #Generar un número aleatorio entre 1 y 100 usando módulo randint
    return random.randint(1,100)

def turno_jugadora1(numeroAleatorio):
   
   #Lista de suposiciones jugadora1 y ordenador
    suposiciones_jugadora1 = []
    suposiciones_ordenador = []

    while True:
        jugadora1 = int(input('Ingrese un número entre 1 y 100: '))
        suposiciones_jugadora1.append(jugadora1)

        if jugadora1 == numeroAleatorio:
         print(f'Correcto! Adivinaste el número secreto {numeroAleatorio}')
         return True, suposiciones_jugadora1, suposiciones_ordenador #Devolver valores cuando la jugadora gane
        elif jugadora1 > numeroAleatorio:
          print(f"Muy alto... El número es más pequeño que {jugadora1}")
          pista = 'menor'
        else:
          print(f"Muy bajo... El número es más grande que {jugadora1}")
          pista = 'mayor'

        #Turno computador
        if pista == 'menor':     
         computador = random.randint(1,jugadora1-1)
        elif pista == 'mayor':
         computador = random.randint(jugadora1 +1, 100) 

        suposiciones_ordenador.append(computador)

        print(f'El turno del ordenador: {computador}')
        if computador == numeroAleatorio:
            print(f'El ordenador ha ganado! El número secreto {numeroAleatorio}')
            return False, suposiciones_jugadora1, suposiciones_ordenador
        elif computador < numeroAleatorio:
            print('El ordenador ha hecho una suposición más baja al número secreto')
        else:
            print('El ordenador ha hecho una suposición más alta al número secreto')
 
        
def juego_numeroSecreto():
  print("Bienvenida! Adivina el número secreto!")
  numeroAleatorio = numero_aleatorio()
  while True: 
    jugador_gano,suposiciones_jugadora1, suposiciones_ordenador = turno_jugadora1(numeroAleatorio)
    if jugador_gano:
            print('Suposiciones del jugador ganador:')
            for suposicion in suposiciones_jugadora1:
                print(suposicion)
    else: 
            print('Suposiciones del ganador ordenador')
            for suposicion in suposiciones_ordenador:
                print(suposicion)

      
    new_play = input('¿Quieres seguir jugando? (S/N): ').upper()
    if new_play != 'S':
            print('Gracias por jugar, Hasta la próxima!') 
            break
    
    
    
juego_numeroSecreto()
    
  



        



