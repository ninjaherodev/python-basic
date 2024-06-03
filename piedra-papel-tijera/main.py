import random
def obtener_eleccion_usuario():
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in ["piedra", "papel", "tijera"]:
        print("Entrada no válida. Inténtalo de nuevo.")
        eleccion = input("Elige piedra, papel o tijera: ").lower()
    return eleccion

def obtener_eleccion_computadora():
    opciones = ("piedra", "papel", "tijera")
    return random.choice(opciones)

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "Perdiste"
    
def jugar_otra_vez():
    respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()
    while respuesta not in ["s", "n"]:
        print("Entrada no válida. Inténtalo de nuevo.")
        respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()
    return respuesta == "s"
    
def jugar():
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    while True:
        usuario = obtener_eleccion_usuario()
        computadora = obtener_eleccion_computadora()
        print(f"Computadora eligió: {computadora}")
        resultado = determinar_ganador(usuario, computadora)
        print(resultado)
        if not jugar_otra_vez():
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    jugar()