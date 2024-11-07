
import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador= input("Ingrese su nombre: ")
    jugador=Jugador(nombre_jugador)
    enemigos= [Enemigo("Alien", 50, 10), 
               Enemigo("Robot", 30, 5), 
               Enemigo("Monstruo", 70, 15)]
    
    enemigos_derrotados= []
    print("Comienza la aventura!!")

    while enemigos: #mientras hayan enemigos en la lista, que se ejecute esto
        enemigo_actual=random.choice(enemigos)
        print(f"Te encuentras frente a {enemigo_actual.nombre}")
        
        if enemigo_actual in enemigos_derrotados:
            continue

        while enemigo_actual.salud > 0:
            accion= input("Que deseas hacer? (atacar/huir): ").lower()
            
            if accion=="atacar":
               dano_jugador= jugador.atacar()
               print(f"Has atacado a {enemigo_actual.nombre} y le has causado {dano_jugador} de daño")
               
               enemigo_actual.recibir_dano(dano_jugador)

               if enemigo_actual.salud > 0:
                   dano_enemigo= enemigo_actual.atacar()
                   print(f"El {enemigo_actual.nombre} te atacó y te causó {dano_enemigo} de daño")
                   jugador.recibir_dano(dano_enemigo)
                   print(f"Te queda {jugador.salud} de salud")
            elif accion == "huir":
                print("Has decidido huir del combate")
                break
                   
        if jugador.salud <= 0:
            print("Has perdido la partida")
            break

        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        jugador.ganar_experiencia(20)

        continuar= input("Quieres seguir explorando?(s/n): ").lower()

        if continuar != "s":
            print("Gracias por haber jugado")
            break
    if not enemigos:
        print("Felicidades has ganado el juego")

if __name__ == "__main__": #solo podemos ejecutar esto desde el archivo principal
    main()