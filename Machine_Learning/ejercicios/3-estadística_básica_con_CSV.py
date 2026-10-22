import math
from pathlib import Path
import pandas as pd 

RUTA_CSV = Path(__file__).parent / "datos_estadistica_alumnos.csv"

print("Solucion del ejercicio 1")
#Carga el archivo CSV en un DataFrame llamado df
df = pd.read_csv(RUTA_CSV)
# Muestra las primeras filas
print(df.head())
# Guarda la columna puntos_prueba en una variable llamada puntos. 
puntos = df["puntos_prueba"].tolist()
# Muestra cuántos datos hay en la columna.
print(f"Cantidad de datos en la columna puntos_prueba: {len(puntos)}")
#  Explica con tus palabras qué representa cada fila del CSV.
print("Cada fila del CSV representa un alumno, con sus datos de nombre, apellido, edad y los puntos obtenidos en una prueba")

print("-------------------------------")

print("Solucion del ejercicio 2")
# Calcula la media de puntos_prueba con el Método 1: bucle for, acumulador y len(). 
suma = 0
for punto in puntos:
    suma += punto
media_bucle = suma / len(puntos)
# Calcula la misma media con el Método 2: sum(), len() y, si quieres practicarlo, map() con lambda
media_funciones = sum(map(lambda x: x, puntos)) / len(puntos)
# Calcula la misma media con el Método 3: pandas usando .mean().
media_pandas = df["puntos_prueba"].mean()
# Muestra los tres resultados con nombres claros: media_bucle, media_funciones y media_pandas
print(f"Media de puntos_prueba (Metodo 1): {media_bucle}")
print(f"Media de puntos_prueba (Metodo 2): {media_funciones}")
print(f"Media de puntos_prueba (Metodo 3): {media_pandas}")
# Explica qué significa esa media en el contexto de la prueba.
print("Como la media (74 puntos) esta muy cerca del centro del rango entre el minimo (50) y el maximo (100), no hay valores extremos que la desplacen hacia un lado. Por eso, la media representa bien el rendimiento tipico del grupo")

print("-------------------------------")

print("Solucion del ejercicio 3")
#  Calcula la mediana de puntos_prueba con el Método 1: 
ordenados_bucle = puntos.copy()
n = len(ordenados_bucle)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if ordenados_bucle[j] > ordenados_bucle[j + 1]:
            ordenados_bucle[j], ordenados_bucle[j + 1] = ordenados_bucle[j + 1], ordenados_bucle[j]
 
if n % 2 == 0:
    centro_izq = ordenados_bucle[n // 2 - 1]
    centro_der = ordenados_bucle[n // 2]
    mediana_bucle = (centro_izq + centro_der) / 2
else:
    mediana_bucle = ordenados_bucle[n // 2]

# Calcula la misma mediana con el Método 2:
ordenados = sorted(puntos)
mitad = len(ordenados) // 2
if len(ordenados) % 2 == 0:
    mediana_funciones = (ordenados[mitad - 1] + ordenados[mitad]) / 2
else:
    mediana_funciones = ordenados[mitad]

# Calcula la misma mediana con el Método 3: pandas usando .median().
mediana_pandas = df["puntos_prueba"].median()
# Muestra los tres resultados con nombres claros: mediana_bucle, mediana_funciones y mediana_pandas
print(f"Mediana de puntos_prueba (Metodo 1): {mediana_bucle}")
print(f"Mediana de puntos_prueba (Metodo 2): {mediana_funciones}")
print(f"Mediana de puntos_prueba (Metodo 3): {mediana_pandas}")
#  Explica por qué la mediana representa el centro de los datos
print("La mediana representa el centro de los datos porque es el valor que divide al conjunto de datos en dos partes iguales, es decir, la mitad de los alumnos obtuvo menos puntos que la mediana y la otra mitad obtuvo más puntos que la mediana. Esto permite tener una idea del rendimiento típico del grupo sin que los valores extremos afecten la medida.")

print("-------------------------------")

print("Solucion del ejercicio 4")
# Calcula la moda de puntos_prueba con el Método 1
frecuencias = {}
for valor in puntos:
    if valor in frecuencias:
        frecuencias[valor] += 1
    else:
        frecuencias[valor] = 1
        
frecuencia_max = 0
for valor in frecuencias:
    if frecuencias[valor] > frecuencia_max:
        frecuencia_max = frecuencias[valor]
        
moda_bucle = []
for valor in frecuencias:
    if frecuencias[valor] == frecuencia_max:
        moda_bucle.append(valor)
        
        
# Calcula la misma moda con el Método 2
valores_unicos = set(puntos)
frecuencia_max_func = max(map(lambda v: puntos.count(v), valores_unicos))
moda_funciones = sorted(filter(lambda v: puntos.count(v) == frecuencia_max_func, valores_unicos))


# Calcula la misma moda con el Método 3
moda_pandas = df["puntos_prueba"].mode().tolist()
 
 
# Muestra los tres resultados con nombres claros: moda_bucle, moda_funciones y moda_pandas
print("moda_bucle:", moda_bucle)
print("moda_funciones:", moda_funciones)
print("moda_pandas:", moda_pandas)

# Comprueba que los tres resultados coinciden
coinciden_moda = moda_bucle == moda_funciones == moda_pandas
print("Coinciden los tres metodos?", coinciden_moda)


# Explica qué significa que ese valor sea la moda
print("La moda representa el valor que aparece con mayor frecuencia en el conjunto de datos. En este caso, el valor", moda_bucle[0], "es la moda porque es el que más veces aparece en la columna 'puntos_prueba'.")


print("-------------------------------")


print("Solucion del ejercicio 5")
# Calcula primero la media de puntos_prueba
media = sum(puntos) / len(puntos)

# Calcula una lista de desviaciones con el Método 1
desviaciones_bucle = []
for valor in puntos:
    desviaciones_bucle.append(valor - media)
    
# Calcula la misma lista con el Método 2
desviaciones_funciones = list(map(lambda valor: valor - media, puntos))

# Calcula las mismas desviaciones con el Método 3
df["desviacion"] = df["puntos_prueba"] - media
desviaciones_pandas = df["desviacion"].tolist()

# Muestra las tres versiones y comprueba que contienen los mismos valores
print("Desviaciones (Método 1):", desviaciones_bucle)
print("Desviaciones (Método 2):", desviaciones_funciones)
print("Desviaciones (Método 3):", desviaciones_pandas)

# Explica qué significa que una desviación sea positiva, negativa o cero
print("la desviación indica cuántos puntos se aleja cada alumno de la media")

print("-------------------------------")

print("\nSolución del ejercicio 6")
# Calcula la varianza de puntos_prueba con el Método 1
suma_cuadrados = 0
for valor in puntos:
    desviacion = valor - media
    suma_cuadrados += desviacion ** 2
varianza_bucle = suma_cuadrados / len(puntos)


# Calcula la misma varianza con el Método 2
varianza_funciones = sum(map(lambda valor: (valor - media) ** 2, puntos)) / len(puntos)


# Calcula la misma varianza con el Método 3
varianza_pandas = df["puntos_prueba"].var(ddof=0)

# Muestra los tres resultados con nombres claros
print("varianza_bucle:", varianza_bucle)
print("varianza_funciones:", varianza_funciones)
print("varianza_pandas:", varianza_pandas)

# Comprueba que los tres resultados coinciden
coinciden_varianza = math.isclose(varianza_bucle, varianza_funciones) and math.isclose(
    varianza_funciones, varianza_pandas
)
print("Coinciden los tres metodos?", coinciden_varianza)


# Explica qué nos dice la varianza sobre el grupo
print(
    f"Un valor de {varianza_bucle:.1f} indica que las notas del grupo no son todas parecidas: hay alumnos\n"
    "bastante por debajo (50, 60) y otros bastante por encima (90, 100). El inconveniente\n"
    "es que está en puntos al cuadrado, así que no se puede comparar directamente con\n"
    "las notas."
)

print("-------------------------------")

print("\nSolución del ejercicio 7")
# Calcula la desviación estándar con el Método 1
desviacion_estandar_bucle = varianza_bucle ** 0.5

# Calcula la misma desviación estándar con el Método 2
desviacion_estandar_funciones = math.sqrt(
    sum(map(lambda valor: (valor - media) ** 2, puntos)) / len(puntos)
)

# Calcula la misma desviación estándar con el Método 3
desviacion_estandar_pandas = df["puntos_prueba"].std(ddof=0)

# Muestra los tres resultados con nombres claros
print("desviacion_estandar_bucle:", desviacion_estandar_bucle)
print("desviacion_estandar_funciones:", desviacion_estandar_funciones)
print("desviacion_estandar_pandas:", desviacion_estandar_pandas)

#  Comprueba que los tres resultados coinciden o que solo cambian por pequeños decimales.
coinciden_desviacion_estandar = math.isclose(
    desviacion_estandar_bucle, desviacion_estandar_funciones
) and math.isclose(desviacion_estandar_funciones, desviacion_estandar_pandas)
print("Coinciden los tres metodos?", coinciden_desviacion_estandar)


#  Explica por qué la desviación estándar es más fácil de interpretar que la varianza
print(
    f"\nInterpretación: la desviación estándar es {desviacion_estandar_bucle:.2f} puntos.\n"
    "Es más fácil de interpretar que la varianza porque está en la misma unidad que los datos\n"
    "(puntos, no puntos al cuadrado). Significa que, de forma típica, las notas de los alumnos\n"
    "se separan unos 14 puntos de la media (74). La mayoría de los alumnos está entre\n"
    "60 y 88 puntos aproximadamente (media ± una desviación estándar)."
)


print("-------------------------------")

print("\nSolución del ejercicio 8")
# Calcula el mínimo y el máximo de puntos_prueba
minimo = min(puntos)
maximo = max(puntos)
rango = maximo - minimo

# Normaliza cada valor con el Método 1
normalizados_bucle = []
for valor in puntos:
    normalizados_bucle.append((valor - minimo) / rango)

# Normaliza los mismos valores con el Método 2
normalizados_funciones = list(
    map(lambda valor: (valor - min(puntos)) / (max(puntos) - min(puntos)), puntos)
)

# Normaliza los mismos valores con el Método 3
columna = df["puntos_prueba"]
df["puntos_normalizados"] = (columna - columna.min()) / (columna.max() - columna.min())
normalizados_pandas = df["puntos_normalizados"].tolist()

# Muestra las tres versiones y comprueba que contienen los mismos valores
print("Normalizados (Método 1):", [round(v, 3) for v in normalizados_bucle])
print("Normalizados (Método 2):", [round(v, 3) for v in normalizados_funciones])
print("Normalizados (Método 3):", [round(v, 3) for v in normalizados_pandas])

# Explica qué significa que un valor normalizado sea 0, 0.5 o 1
print(
    "\nInterpretación: la normalización lleva todos los valores al rango [0, 1].\n"
    "- 0 significa que el alumno tiene el valor mínimo del grupo (Ana, 50 puntos).\n"
    "- 1 significa que el alumno tiene el valor máximo del grupo (Lucía, 100 puntos).\n"
    "- 0.5 significa que el valor está justo en el centro entre el mínimo y el máximo\n"
)


print("-------------------------------")

print("\nSolución del ejercicio 9")
# Calcula la media y la desviación estándar de puntos_prueba
desviacion_estandar = desviacion_estandar_bucle

# Estandariza cada valor con el Método 1
estandarizados_bucle = []
for valor in puntos:
    estandarizados_bucle.append((valor - media) / desviacion_estandar)

# Estandariza los mismos valores con el Método 2
estandarizados_funciones = list(map(lambda valor: (valor - media) / desviacion_estandar, puntos))

# Estandariza los mismos valores con el Método 3
df["puntos_estandarizados"] = (columna - columna.mean()) / columna.std(ddof=0)
estandarizados_pandas = df["puntos_estandarizados"].tolist()

# Muestra las tres versiones y comprueba que contienen los mismos valores.
print("z-score (Método 1):", [round(v, 3) for v in estandarizados_bucle])
print("z-score (Método 2):", [round(v, 3) for v in estandarizados_funciones])
print("z-score (Método 3):", [round(v, 3) for v in estandarizados_pandas])
print(
    "Media de los z:", round(df["puntos_estandarizados"].mean(), 10),
    "| Desviación estándar de los z:", round(df["puntos_estandarizados"].std(ddof=0), 10),
)

# Explica qué significa que un valor z sea positivo, negativo o cercano a 0
print(
    "\nInterpretación: el z-score indica a cuántas desviaciones estándar está cada alumno de la media.\n"
    "- z positivo: por encima de la media\n"
    "- z negativo: por debajo de la media\n"
    "- z cercano a 0: muy cerca de la media\n"
)

print("-------------------------------")

print("\nSolución del ejercicio 10")
nombres = df["nombre"].tolist()
# Indica qué alumnos están por encima de la media usando el Método 1
encima_bucle = []
for nombre, valor in zip(nombres, puntos):
    if valor > media:
        encima_bucle.append(nombre)
        
# Indica los mismos alumnos usando el Método 2
encima_funciones = list(
    map(lambda par: par[0], filter(lambda par: par[1] > media, zip(nombres, puntos)))
)

#  Indica los mismos alumnos usando el Método 3
encima_pandas = df[df["puntos_prueba"] > media]["nombre"].tolist()

print("Por encima de la media (Método 1):", encima_bucle)
print("Por encima de la media (Método 2):", encima_funciones)
print("Por encima de la media (Método 3):", encima_pandas)

# Indica qué alumnos están por debajo de la media usando también los tres métodos
# Método 1
debajo_bucle = []
for nombre, valor in zip(nombres, puntos):
    if valor < media:
        debajo_bucle.append(nombre)
        
# Método 2
debajo_funciones = list(
    map(lambda par: par[0], filter(lambda par: par[1] < media, zip(nombres, puntos)))
)

# Método 3
debajo_pandas = df[df["puntos_prueba"] < media]["nombre"].tolist()

print("\nPor debajo de la media (Método 1):", debajo_bucle)
print("Por debajo de la media (Método 2):", debajo_funciones)
print("Por debajo de la media (Método 3):", debajo_pandas)


# Indica qué alumno o alumnos tienen el valor normalizado más alto
# Indica qué alumno o alumnos tienen el valor normalizado más bajo.
norm = df["puntos_normalizados"]
alumnos_norm_max = df[norm == norm.max()]["nombre"].tolist()
alumnos_norm_min = df[norm == norm.min()]["nombre"].tolist()
print("\nValor normalizado más alto:", norm.max(), "->", alumnos_norm_max)
print("Valor normalizado más bajo:", norm.min(), "->", alumnos_norm_min)

# Indica si hay algún valor que parezca especialmente alejado del resto
alejados = df[df["puntos_estandarizados"].abs() > 2]["nombre"].tolist()
print("\nAlumnos con |z| > 2:", alejados if alejados else "ninguno")
print(
    "z más extremos:",
    round(df["puntos_estandarizados"].min(), 2), "(mínimo) y",
    round(df["puntos_estandarizados"].max(), 2), "(máximo)",
)

# Escribe una conclusión breve sobre el rendimiento general del grupo
print()
print(df[["nombre", "puntos_prueba", "desviacion", "puntos_normalizados", "puntos_estandarizados"]].round(2))

print(
    "\nConclusión: el rendimiento general del grupo es bueno. La media es 74 puntos y la\n"
    "mediana 75, muy parecidas, y el resultado más frecuente es 80. La mitad del grupo\n"
    "(5 alumnos) está por encima de la media y la otra mitad por debajo. La desviación\n"
    "estándar de 14.28 puntos indica una dispersión moderada: hay diferencias entre\n"
    "alumnos, pero ningún valor es extremo, ya que todos los z-score están entre -1.68\n"
    "y +1.82. Lucía tiene el mejor resultado (100) y Ana el más bajo (50); Ana es la\n"
    "alumna que más apoyo podría necesitar."
)