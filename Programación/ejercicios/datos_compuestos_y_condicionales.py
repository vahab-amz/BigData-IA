# Ejercicio 1. Listas: control de notas
print("Solucion del ejercicio 1")
notas = [6,8,5,9,7]
primera_nota = notas[0]
ultima_nota = notas[-1]
notas[1] = 10
notas.append(8)
total_notas = len(notas)
print(f"Primera nota: {primera_nota}")
print(f"Ultima nota: {ultima_nota}")
print(f"Notas actualizadas: {notas}")
print("\n")


# Ejercicio 2. Tuplas: datos fijos de un producto
print("Solucion del ejercicio 2")
producto = ("Laptop", 1200.50, 12)
nombre = producto[0]
precio = producto[1]
unidades = producto[2]
valor_total = precio * unidades
print(f"Nombre del producto: {nombre}")
print(f"Precio: {precio}")
print(f"Unidades: {unidades}")
print(f"valor total del stock: {valor_total}")
print("\n")


# Ejercicio 3. Diccionarios: ficha de alumno
print("Solucion del ejercicio 3")
alumno ={
    "nombre": "Vau",
    "edad": 27,
    "curso": "AI y Big Data",
    "nota" : 9.5
}
print(f"Nombre del alumno: {alumno['nombre']}")
print(f"Nota del alumno: {alumno['nota']}")
alumno["nota"] = 10
alumno["aprobado"] = alumno["nota"] >= 5
print(alumno, "\n")


# Ejercicio 4. Conjuntos: usuarios registrados
print("Solucion del ejercicio 4")
usuarios = {"Ana", "Luis", "Marta", "Ana", "Pedro"}
nuevo_usuario = "Luis"
usuario_existe = nuevo_usuario in usuarios
usuarios.add("Clara")
total_usuarios = len(usuarios)
print(f"Usuario nuevo existe: {usuario_existe}")
print(f"Total de usuarios: {total_usuarios}")
print("\n")


# Ejercicio 5. Condiciones con and, or y not
print("Solucion del ejercicio 5")
edad = 27
tiene_permiso = True
es_socio = True
sancionado = False
acceso_por_edad = edad < 16 and tiene_permiso
acceso_por_socio = es_socio and not sancionado
puede_acceder = acceso_por_edad or acceso_por_socio
print(f"Acceso por edad: {acceso_por_edad}")
print(f"Acceso por socio: {acceso_por_socio}")
print(f"Puede acceder: {puede_acceder}")
print("\n")


# Ejercicio 6. if, elif y else: clasificación de matrícula
print("Solucion del ejercicio 6")
nota_media = 7.5
renta_baja = False
familia_numerosa = False
mensaje = ""
if nota_media < 5:
    mensaje = "No admitido"
elif nota_media >= 9:
    mensaje = "Beca completa"
elif nota_media >= 7 and (renta_baja or familia_numerosa):
    mensaje = "Beca parcial"
elif nota_media >= 5:
    mensaje = "Admitido sin beca"
else:
    mensaje = "Revisar solicitud"
print(mensaje, "\n")


# Ejercicio 7. Ternaria: mensaje de resultado
print("Solucion del ejercicio 7")
nota = 8
resultado = "Aprobado" if nota >= 5 else "Suspenso"
tipo_nota = "Alta" if nota >= 8 else "Normal" 
print(f"Nota: {nota}")
print(f"Resultado: {resultado}")
print(f"Tipo de nota: {tipo_nota}")
print("\n")


# Ejercicio 8. match-case: menú de aplicación
print("Solucion del ejercicio 8")
opcion = "crear"
mensaje = ""
match opcion:
    case "crear":
        mensaje = "Creando registro"
    case "editar":
        mensaje = "Editando registro"
    case "borrar":
        mensaje = "Borrando registro"
    case "listar":
        mensaje = "Mostrando registros"
    case _:
        mensaje = "Opcion no reconocida"
print(mensaje, "\n")


# Ejercicio 9. Caso completo: pedido online
print("Solucion del ejercicio 9")
productos = ["airpods", "laptop", "smartphone"]
precios = [150, 1200, 800]
cliente = {
    "nombre": "Vau",
    "es_socio": True,
    "saldo": 5800
}
cupones_validos = {"DESCUENTO10", "DESCUENTO20", "DESCUENTO30"}
cupon_usado = "DESCUENTO20"
precio_total = sum(precios)
tiene_descuento = cupon_usado in cupones_validos or cliente["es_socio"]
if tiene_descuento:
    total_final  = 0.1 * precio_total
else:
    total_final = precio_total

if cliente["saldo"] >= total_final:
    mensaje = "Pedido aceptado"
else:  
    mensaje = "Saldo insuficiente"
print(f"nombre del cliente: {cliente['nombre']}")
print(f"productos: {productos}")
print(f"precio total: {precio_total}")
print(f"mensaje: {mensaje}")
print("\n")


# Ejercicio 10. Caso completo: evaluación de acceso
print("Solucion del ejercicio 10")
requisitos = (18, 7, True)
candidato = {
    "nombre": "Vahab",
    "edad": 27,
    "nota": 9,
    "permiso": True
}
cursos_disponibles = {"Python", "Big Data", "IA"}
curso_elegido = "Big Data"
curso_existe = curso_elegido in cursos_disponibles
cumple_edad = candidato["edad"] >= requisitos[0]
cumple_nota = candidato["nota"] >= requisitos[1]
if requisitos[2]:
    cumple_permiso = candidato["permiso"]
else:
    cumple_permiso = True
if not curso_existe:
    mensaje = "Curso no disponible"
elif cumple_edad and cumple_nota and cumple_permiso:
    mensaje = "Acceso concedido"
elif candidato["nombre"] == "" or curso_elegido == "":
    mensaje = "Solicitud incompleta"
else:
    mensaje = "No cumple requisitos"
estado = "Apto" if mensaje == "Acceso concedido" else "No apto"
print(f"Nombre: {candidato["nombre"]}")
print(f"Curso elegido: {curso_elegido}")
print(f"Estado: {estado}")
print(f"Mensaje: {mensaje}")
