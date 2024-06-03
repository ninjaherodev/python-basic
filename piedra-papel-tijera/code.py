import random

opciones = ('piedra', 'papel', 'tijera')
opciones_texto = ', '.join(opciones).title()


def userOption() -> str:
    eleccion = input(f"Elige: [ {opciones_texto} ]: ").lower()
    while eleccion not in opciones:
     print("Entrada no válida. Inténtalo de nuevo.")
     eleccion = input(f"Elige {opciones_texto}: ").lower()
    return eleccion

def cpuOption() -> str:
    return random.choice(opciones)


def win(opcUser, opcCpu) -> str:
   if opcUser == opcCpu :
      return "!Empate"
   elif ((opcUser == 'piedra' and opcCpu=='tijera') or 
         (opcUser == 'papel'  and opcCpu=='piedra') or
         (opcUser == 'tijera' and opcCpu=='papel')
         ):
       return 'Ganaste!'
   else: 
      return 'Perdiste!'
   
def playAgain() -> bool:
   response = input('¿Quieres jugar otra vez? (s/n):').lower()
   while response not in ['s', 'n']:
      print("Entrada no válida. Inténtalo de nuevo.")
      response = input("¿Quieres jugar otra vez? (s/n): ").lower()
   return response == "s" 
   
def game():
   print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
   while True:
    usuario = userOption()
    computadora = cpuOption()
    print(f"Computadora eligió: {computadora}")
    resultado = win(usuario, computadora)
    print(resultado)
    if not playAgain():
        print("¡Gracias por jugar!")
        break


if __name__ == "__main__":
    game()