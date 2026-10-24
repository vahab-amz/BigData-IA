print("Solucion del ejercicio 1")
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
coche_1 = Coche("Mercedes", "Maybach")
coche_2 = Coche("Rolls Royce", "Phantom")
print(f"La marca: {coche_1.marca}, el modelo: {coche_1.modelo}")
print(f"La marca: {coche_2.marca}, el modelo: {coche_2.modelo}")
coche_1.modelo = "G Wagon"
print(f"La marca: {coche_1.marca}, el modelo: {coche_1.modelo}")
print(f"La marca: {coche_2.marca}, el modelo: {coche_2.modelo}")

print("--------------------------------")

print("Solucion del ejercicio 2")
class CochePruebas:
    def __init__(self, velocidad):
        self.velocidad = velocidad
    
    def acelerar(self):
        if self.velocidad < 0:
            return False
        self.velocidad += 10

    def detener(self):
        if self.velocidad < 0:
            return False
        self.velocidad = 0
        
coche_prueba_1 = CochePruebas(450)
coche_prueba_2 = CochePruebas(300)
coche_prueba_2.detener()
print(f"Coche 1 tiene el velocidad {coche_prueba_1.velocidad} km/h")
print(f"Coche 2 tiene el velocidad {coche_prueba_2.velocidad} km/h")

print("--------------------------------")

print("Solucion del ejercicio 3")
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def describir(self):
        return f"Este coche es de la marca {self.marca} y el modelo es el {self.modelo}"
        
class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km
        

coche_electrico = CocheElectrico("Tesla", "Model Y", 201)
print(coche_electrico.marca)         
print(coche_electrico.modelo)        
print(coche_electrico.autonomia_km)  
print(coche_electrico.describir())

print("--------------------------------")

print("Solucion del ejercicio 4")
class Motor:
    def __init__(self, modelo):
        self.modelo = modelo

    def arrancar(self):
        return "Motor en marcha"

class MotorGasolina(Motor):
    def arrancar(self):
        return "Motor de gasolina en marcha"

class MotorElectrico(Motor):
    def arrancar(self):
        return "Motor eléctrico en marcha"

coche_tesla = MotorElectrico("Model Y")
coche_bmw = MotorGasolina("M4")

print(f"El coche {coche_tesla.modelo}: {coche_tesla.arrancar()}")
print(f"El coche {coche_bmw.modelo}: {coche_bmw.arrancar()}")

print("--------------------------------")

print("Solucion del ejercicio 5")
def poner_en_marcha(motor):
    return motor.arrancar()

lista_de_coche = [coche_tesla, coche_bmw]
for coche in lista_de_coche:
    print(poner_en_marcha(coche))

class MotorDiesel(Motor):
    def arrancar(self):
        return "Motor diésel en marcha"
    
coche_mercedes = MotorDiesel("300D")
lista_de_coche.append(coche_mercedes)
for coche in lista_de_coche:
    print(poner_en_marcha(coche))
    
print("--------------------------------")

print("Solucion del ejercicio 6")
class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km
        
    def describir(self):
        describir = super().describir()
        return f"{describir}. Autonomia: {self.autonomia_km} km"
    
coche_electrico2 = CocheElectrico("Porsche", "Taycan Turbo GT", 305)
print(coche_electrico2.marca)         
print(coche_electrico2.modelo)        
print(coche_electrico2.autonomia_km)  
print(coche_electrico2.describir())

print("--------------------------------")

print("Solucion del ejercicio 7")
marca = "BMW"
modelo = "i7 M70 xDrive"
anio = 2026
print(f"El coche es un {marca} {modelo} del año {anio}")

marca = "Audi"
modelo = "RS e-tron GT performance"
anio = 2026
print(f"El coche es un {marca} {modelo} del año {anio}.")

print("--------------------------------")

print("Solucion del ejercicio 8")
try:
    km = int(input("Kilómetros recorridos: "))
    print("Kilómetros indicados:", km)
except ValueError:
    print("Debes escribir un número entero.")

print("Programa finalizado.")