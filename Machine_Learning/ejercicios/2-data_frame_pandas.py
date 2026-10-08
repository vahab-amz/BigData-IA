import pandas as pd
import numpy as np

def separador():
    print("-------------------------------")




# Ejercicio 1. Crear la estructura de datos
alumnos = {
    "Nombre": ["Ana", "Paco", "Marta", "Luis", "Elena", "Carlos", "Sara", "Miguel", "Lucia", "Andres"],
    "Edad": [23, 21, 19, 25, 22, 20, 18, 27, 21, 24],
    "Puntos": [43, 38, 41, 35, 39, 36, 34, 45, 42, 37],
    "Estudios superiores": [True, False, True, False, True, True, False, False, True, False]
}


# Ejercicio 2. Crear un DataFrame
df = pd.DataFrame(alumnos)
print(df,"\n")


#Ejercicio 3. Explorar el DataFrame
print("Muestra las primeras filas del DataFrame", "\n" ,df.head()) 
separador()
print("Muestra el tamano del DataFrame", "\n" ,df.shape)
separador()
print("Muestra la informacion del DataFrame", "\n" ,df.info())
separador()
print("Muestra las estadisticas del DataFrame", "\n" ,df.describe())
separador()
print("Muestra los nombres de las columnas del DataFrame", "\n" ,df.columns)
separador()
print("Muestra los tipos de datos de las columnas del DataFrame", "\n" ,df.dtypes)
separador()



# Ejercicio 4. Crear una regla de selección
condicion_1 = (df["Edad"] >= 22) & (df["Puntos"] > 40)
condicion_2 = (df["Edad"] < 22) & (df["Estudios superiores"] == True) & (df["Puntos"] >= 40)


# Ejercicio 5. Añadir una nueva columna
df["apto"] = np.where(condicion_1 | condicion_2, True, False)
print("Muestra el DataFrame con la nueva columna", "\n" ,df)


# Ejercicio 6. Contar personas aptas y no aptas
aptas = df[df["apto"] == True]
no_aptas = df[df["apto"] == False]

print("Numero de personas aptas:", len(aptas))
print("Numero de personas no aptas:", len(no_aptas))
print("\n")


# Ejercicio 7. Filtrar candidatos aptos
candidatos_aptos = df[df["apto"] == True]
print("Candidatos aptos:", "\n" ,candidatos_aptos)
print("\n")

# Ejercicio 8. Filtrar candidatos con estudios superiores
candidatos_estudios_superiores = df[df["Estudios superiores"] == True]
numero_de_candidatos_estudios_superiores = len(candidatos_estudios_superiores)
print("numero de candidatos con estudios superiores:", numero_de_candidatos_estudios_superiores)
candidatos_estudios_superiores_apto = candidatos_estudios_superiores[candidatos_estudios_superiores["apto"] == True]
numero_de_candidatos_estudios_superiores_apto = len(candidatos_estudios_superiores_apto)
print("numero de candidatos con estudios superiores y aptos:", numero_de_candidatos_estudios_superiores_apto)
if numero_de_candidatos_estudios_superiores > numero_de_candidatos_estudios_superiores_apto:
    print("Hay candidatos con estudios superiores que no son aptos")
else:
    print("Todos los candidatos con estudios superiores son aptos")
print("\n")

# Ejercicio 9. Ordenar los candidatos
puntacion_menor_a_mayor = df.sort_values(by="Puntos", ascending=True)
print("Ordenado de menor a mayor puntuacion:" , "\n" , puntacion_menor_a_mayor)
puntacion_mayor_a_menor = df.sort_values(by="Puntos", ascending=False)
print("Ordenado de mayor a menor puntuacion:" , "\n" , puntacion_mayor_a_menor)
print("\n")


# Ejercicio 10. Calcular estadísticas
print("Estadisticas de los puntos:")
edad_media = df["Edad"].mean()
print("Edad media:", edad_media)
puntuacion_media = df["Puntos"].mean()
print("Puntuacion media:", puntuacion_media)
puntuacion_maxima = df["Puntos"].max()
print("Puntuacion maxima:", puntuacion_maxima)
puntuacion_minima = df["Puntos"].min()
print("Puntuacion minima:", puntuacion_minima)
edad_mas_joven = df["Edad"].min()
print("Edad del mas joven:", edad_mas_joven)
edad_mas_mayor = df["Edad"].max()
print("Edad del mas mayor:", edad_mas_mayor)
print("\n")


# Ejercicio 11. Crear una columna de nivel
def calcular_nivel(puntos):
    if puntos >= 40:
        return "alto"
    elif puntos >= 35:
        return "medio"
    else:
        return "bajo"

df["nivel"] = df["Puntos"].apply(calcular_nivel)
print("DataFrame con la nueva columna 'Nivel':", "\n", df)
print("\n")


# Ejercicio 12. Agrupar por nivel
grupos = df.groupby("nivel")
print("Agrupacion por nivel:", "\n", grupos.size())
print("Edad media por nivel:", "\n", grupos["Edad"].mean())
print("Puntuacion media por nivel:", "\n", grupos["Puntos"].mean()) 
print("\n")


# Ejercicio 13. Seleccionar columnas concretas
resumen_candidatos = df[["Nombre", "Puntos", "apto"]]
print("Resumen de candidatos:", "\n", resumen_candidatos)
print("\n")


# Ejercicio 14. Renombrar columnas
df_renombrado = df.rename(columns={
    "nombre": "Nombre del candidato",
    "edad": "Edad",
    "puntos": "Puntuacion",
    "estudios_superiores": "Estudios superiores",
    "apto": "Es apto?",
    "nivel": "Nivel",
})
print(df_renombrado)
print("\n")
