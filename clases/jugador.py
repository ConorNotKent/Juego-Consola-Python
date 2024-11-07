import random


class Jugador:
    def __init__(self, nombre):
        self.nombre=nombre
        self.salud=100 #no hace falta que esto me los digan ahi arriba porque empiezan fijos
        self.nivel=1
        self.experiencia= 0

    def atacar(self):
        return random.randint(10, 20)* self.nivel #mientras el nivel sea mas alto, mas daño al oponente
    
    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud <= 0:
            print(f"{self.nombre} ha muerto")
            

    def ganar_experiencia(self, experiencia):
        self.experiencia += experiencia
        print(f"{self.nombre} ha ganado {experiencia} puntos de experiencia")
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia = 0
            print(f"{self.nombre} ha subido al nivel {self.nivel}")
