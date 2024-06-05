import random
from colorama import init, Fore, Back, Style # type: ignore
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


def findWinner(opcUser, opcCpu) -> str:
   if opcUser == opcCpu :
      return "empate"
   elif ((opcUser == 'piedra' and opcCpu=='tijera') or 
         (opcUser == 'papel'  and opcCpu=='piedra') or
         (opcUser == 'tijera' and opcCpu=='papel')
         ):
       return "usuario"
   else: 
      return "computador"
   
def playAgain() -> bool:
   response = input('¿Quieres jugar otra vez? (s/n):').lower()
   while response not in ['s', 'n']:
      print("Entrada no válida. Inténtalo de nuevo.")
      response = input("¿Quieres jugar otra vez? (s/n): ").lower()
   return response == "s" 
   
def game():
   print("¡Bienvenido al juego de Piedra, Papel o Tijera!\n")
   rondas = 3
   user_win = 0
   cpu_win = 0
   rondas_jugadas = 0

   while True:
    print(f"Ronda [{rondas_jugadas + 1}] de [{rondas}]")
    print(f"*****************\n")
    usuario = userOption()
    computadora = cpuOption()
    print(f"Computadora eligió: {computadora}")
    resultado = findWinner(usuario, computadora)
    if resultado == "usuario":
       user_win += 1
       print(Fore.GREEN + 'Ganaste!'+ Style.RESET_ALL)
    elif resultado == "computador":
       cpu_win+=1
       print(Fore.RED+'Perdiste!'+ Style.RESET_ALL)
    else:
       print(resultado)   

    rondas_jugadas += 1
    print(f"Marcador => cpu: {cpu_win} user: {user_win}\n" )
    
    if rondas_jugadas>= rondas:
        print("¡Gracias por jugar!")
        print(f"Rondas jugadas: {rondas_jugadas}")
        print(f"Victorias del usuario: {user_win}")
        print(f"Victorias de la computadora: {cpu_win}")
        if user_win > cpu_win:
           print("¡El usuario es el ganador final!")
        elif user_win < cpu_win:
           print("¡La computadora es la ganadora final!")
        else:
           print("¡Es un empate final!")
        break


if __name__ == "__main__":
    game()