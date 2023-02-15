#1Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehicle:

    def __init__(self, velocidad_maxima: float, kilometraje: float):

        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

#2Cree una clase Punto que represente un punto en el plano cartesiano.

"""3 A la clase del punto anterior, defínale los siguientes métodos:
- Un método mostrar que imprima por consola las coordenadas del punto
- Un método mover que cambie las coordenadas del punto
- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
"""


import math


class Punto:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def getter(self):
        print(f"su punto coordenado en R2 seria: {self.x},{self.y}")

    def setter(self):
        self.x = eval(input("introduzca el nuevo valor de x"))
        self.y = eval(input("introduzca el nuevo valor de y"))

    def distancia(self, otro_punto):
        distancia_x = self.x - otro_punto.x
        distancia_y = self.y - otro_punto.y
        return math.sqrt(distancia_x ** 2 + distancia_y ** 2)

#4 Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a
#la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.


class Rectangulo:

    def __init__(self, largo: int, ancho: int):
        self.largo = largo
        self.ancho = ancho

    def perimetro(self):
        perimetro = (2*self.largo)+(2*self.ancho)
        print("el perimetro de su figura es: ", perimetro)
        return perimetro

    def area(self):
        area = self.largo * self.ancho

        if self.largo == self.ancho:
            print("su figura geoemetrica es un rectangulo cuadrado y su area es: ", area)
            return area

#5 Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor.
#Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.


class Circulo:

    def __init__(self, radio: float, centro_x: float, centro_y: float):
        self.radio = radio
        self.centro_x = centro_x
        self.diametro = 2 * self.radio
        self.centro_y = centro_y

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def pertenencia(self, punto_x: int, punto_y: int):
        distancia_x = punto_x - self.centro_x
        distancia_y = punto_y - self.centro_y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        if distancia > self.radio:
            print("su punto no esta en la circunferencia")
            return distancia
        elif distancia <= self.radio:
            print("su punto esta en la circunferencia")
            return distancia


#6 Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto
#se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.

class Carta:
    PINTAS = ("Corazones", "Diamantes", "Tréboles", "Picas")
    VALORES = ("A", "J", "Q", "K", "diez", "nueve", "ocho", "siete", 'seis', 'cinco', 'cuatro', 'tres', 'dos')

    def __init__(self, valor: str, pinta: str):
        self.pinta = pinta
        self.valor = valor


#7 propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta,

#8 Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.

#9 Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.

#10 Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta

#11 Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.

class CuentaBancaria:

    def __init__(self, numero_cuenta: int, propietarios: str,  balance: int):

        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, valor: int):
        self.balance += valor

    def retirar(self, valor: int):
        self.balance -= valor

    def aplicar_cuota_manejo(self, porcentaje=0.02):
        tarifa = porcentaje * self.balance
        self.balance += tarifa

    def mostrar_detalles(self):
        print(f"los detalles de su cuenta son los siguientes ,\n"
              f"su numero de cuenta bancaria es: {self.numero_cuenta},\n"
              f"los propietarios de dicha cuenta son: {self.propietarios},\n"
              f"el balance total de la cuenta antes de la cuota de manejo es: {self.balance},\n"
              f"despues de la cuota seria { self.aplicar_cuota_manejo() }")