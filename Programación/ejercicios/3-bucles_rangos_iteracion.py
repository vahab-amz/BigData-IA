# Ejercicio 1. Control de notas
notas = [7, 5, 8, 6, 9, 4, 10, 3, 2]
#  Mostrar todas las notas.
for nota in notas:
    print(nota)
# Calcular cuántas notas están aprobadas y cuántas suspendidas
num_aprobados = 0
num_suspensos = 0    
for nota in notas:
    if nota >= 5:
        num_aprobados += 1
    else:
        num_suspensos += 1
print(f"Numero de aprobados: {num_aprobados}")
print(f"Numero de suspensos: {num_suspensos}")
# Calcular la nota media.
nota_media = sum(notas) / len(notas)
print(f"Nota media: {nota_media}")
# Mostrar la nota más alta y la nota más baja.
nota_mas_alta = 0
nota_mas_baja = 10
for nota in notas:
    if nota > nota_mas_alta:
        nota_mas_alta = nota
    if nota < nota_mas_baja:
        nota_mas_baja = nota
print(f"Nota mas alta: {nota_mas_alta}")
print(f"Nota mas baja: {nota_mas_baja}")
# Indicar si la media final está aprobada o suspendida.
if nota_media >= 5:
    print("La media es aprobada")
else:
    print("La media es suspendida")
print("\n")


# Ejercicio 2. Carrito de la compra
productos = ["pollo", "carne", "leche", "huevos"]
precios = [5.5, 8.0, 1.2, 2.5]
#  Mostrar cada producto con su precio.
for producto, precio in zip(productos, precios):
    print(producto,precio)
# Calcular el precio total de la compra.
# Aplicar un descuento del 10% si el total supera 20 euros.
precio_total = 0
for precio in precios:
    precio_total += precio  
if precio_total > 20:
    precio_total *= 0.9
# Mostrar el total final que debe pagarse.
print(f"El precio que hay que pagar es: {precio_total}")    
print("\n")


# Ejercicio 3. Registro de alumno
alumno = {
    "nombre": "Vau",
    "edad": 27,
    "curso": "Python",
    "nota_media": 9.5,
    "faltas": 2
}
# Mostrar todos los datos del alumno.
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")
# Indicar si el alumno aprueba. Aprueba si su nota_media es mayor o igual que 5.
# Indicar si debe recibir un aviso. Recibe aviso si tiene más de 10 faltas.
aprobado = False
aviso = False
if alumno["nota_media"] >= 5:
    print("El alumno ha aprobado")
    aprobado = True
if alumno["faltas"] > 10:
    print("Tiene demasiadas faltas")
    aviso = True
# Mostrar un mensaje final combinando el resultado académico y el aviso por faltas.
if aprobado and aviso:
    print("El alumno aprueba, pero debe recibir un aviso por faltas.")
elif aprobado and not aviso:
    print("El alumno aprueba y no debe recibir un aviso.")
elif not aprobado and aviso:
    print("El alumno suspende y debe recibir un aviso por faltas.")
else:
    print("El alumno suspende y no debe recibir un aviso.")
print("\n")


# Ejercicio 4. Números pares, impares y múltiplos
# Contar cuántos números son pares.
num_pares = 0
for i in range(1, 51):  
    if i % 2 == 0:
        num_pares += 1
# Contar cuántos números son impares.
num_impares = 0
for i in range(1, 51):
    if i % 2 != 0:
        num_impares += 1    
# Contar cuántos números son múltiplos de 5
num_multiplos_5 = 0
for i in range(1, 51):
    if i % 5 == 0:
        num_multiplos_5 += 1
# Mostrar los tres resultados finales.
print(f"Numeros pares: {num_pares}")
print(f"Numeros impares: {num_impares}")
print(f"Multiplos de 5: {num_multiplos_5}")
print("\n")


# Ejercicio 5. Validación de contraseña
password = "python_is_fun"
# Comprobar si la contraseña tiene al menos 8 caracteres.
mas_de_8 = len(password) >= 8
# Comprobar si contiene el símbolo @
contiene_arroba = "@" in password
# Comprobar que no sea igual a 12345678.
no_es_12345678 = password != "12345678"
if mas_de_8 and contiene_arroba and no_es_12345678:
    print("Contraseña valida")
else:
    print("Contraseña no valida")
print("\n") 
    
# Ejercicio 6. Inventario de productos
# Crea un diccionario donde las claves sean nombres de productos y los valores sean las unidades disponibles.
inventario = {
    "pantalones": 10,
    "camiseta": 5,
    "zapatillas": 8,
    "gorra": 3
}
# Mostrar todos los productos y sus unidades.
for producto, unidades in inventario.items():
    print(f"{producto}: {unidades} unidades")
# Mostrar qué productos están agotados.
print("Productos agotados:")
estan_agotados = False
for producto, unidades in inventario.items():
    if unidades == 0:
        print(f"- {producto}")
        estan_agotados = True
if not estan_agotados:
    print("No hay productos agotados.")
# Calcular cuántas unidades hay en total.
total_unidades = sum(inventario.values())
# Mostrar cuántos productos tienen menos de 10 unidades.
pocos_stock = 0
for producto, unidades in inventario.items():
    if unidades < 10:
        pocos_stock += 1
print(f"Productos con menos de 10 unidades: {pocos_stock}", '\n')


# Ejercicio 7. Búsqueda en una lista
# Crea una lista de nombres de alumnos y una variable con el nombre que se quiere buscar.
alumnos = ["Martin", "Alex", "Onai", "Andres", "Pau" , "Vau", "isac"]
nombre_busqueda = "Vau"
# Recorrer la lista buscando ese nombre.
# Si encuentra el nombre, mostrar en qué posición está.
# Cuando lo encuentre, detener la búsqueda.
encontrado = False
for posicion, nombre in enumerate(alumnos):
    if nombre == nombre_busqueda:
        print(f"El nombre se encuentra en la posición {posicion}.")
        encontrado = True
        break
if not encontrado:
    print("Alumno no encontrado")
print("\n")


# Ejercicio 8. Limpieza de datos
# Crea una lista con varios números, incluyendo positivos, negativos y ceros.
numeros = [5, -3, 7, 8, -1, 0, 2]
sum_num_positivos = 0
num_ceros = 0
for num in numeros:
    if num < 0:
        continue
    elif num == 0:
        num_ceros += 1
    else:
        sum_num_positivos += num
print(f"Suma de numeros positivos: {sum_num_positivos}")
print(f"Numeros ceros: {num_ceros}")
print("\n")


# Ejercicio 9. Clasificación de usuarios
# Crea una lista de diccionarios. Cada diccionario representa un usuario con los siguientes datos:
usuarios = [
    {"nombre": "Vau", "edad": 27, "activo": True, "puntos": 150},
    {"nombre": "Juan", "edad": 17, "activo": True, "puntos": 80},
    {"nombre": "Carlos", "edad": 30, "activo": False, "puntos": 150},
    {"nombre": "Laura", "edad": 16, "activo": True, "puntos": 110}  
]
for usuario in usuarios:
    if not usuario["activo"]:
        calificacion = "Inactivo"
    elif usuario["puntos"] >= 100:
        calificacion = "Premium"
    else: 
        calificacion = "Estandar"
        
    if usuario["edad"] < 18:
        calificacion += " (Menor de edad)"
for usuario in usuarios:
    print(f"Nombre: {usuario['nombre']}, Calificacion: {calificacion}")
print("\n")


# Ejercicio 10. Sistema de intentos
# Crea una variable codigo_correcto y una lista llamada intentos con varios códigos introducidos.
codigo_correcto = "1234"
intentos = ["5678", "1234", "9012", "1234"]
acceso = False
for intento in intentos:
    print("Intento:", intento)
    if intento == "":
        pass
    if intento == codigo_correcto:
        print("Acceso concedido")
        acceso = True
        break
if not acceso:
    print("Acceso denegado")
print("\n")


# Ejercicio 11. Diferencia/similitudes : "i=i+1", "i++", "++i", i+=1
print("En Python la forma correcta de incrementar una variable es usando 'i += 1' o 'i = i + 1' y no existe la sintaxis 'i++' o '++i'", '\n')
print('ejemplo:')
i = 0
while i < 5:
    print(i)
    i += 1 # o i = i + 1

# Ejercicio 12. "zip" y "enumerate" en iteradores
print("En Python, 'zip' se utiliza para combinar dos o más iterables en un solo iterable de tuplas, mientras que 'enumerate' se utiliza para obtener tanto el índice como el valor de los elementos de un iterable.")
print('ejemplo de zip:')
nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 35]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")    
print('ejemplo de enumerate:')
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas):
    print(f"Fruta {indice}: {fruta}")