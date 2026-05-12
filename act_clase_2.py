import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 10)
    intentos = 0
    ganado = False

    print("¡Bienvenido al juego de adivinanza!")
    print("He pensado un número entre 1 y 10. ¿Puedes adivinarlo?")

    while not ganado:
        try:
            suposicion = int(input("Introduce tu número: "))
            intentos += 1

            if suposicion < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif suposicion > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste en {intentos} intentos.")
                ganado = True
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    adivina_el_numero()