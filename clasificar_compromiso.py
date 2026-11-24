
# Programa: Clasificacion del compromiso de sesiones de clientes

# Funcion para clasificar el nivel de compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Matriz con los datos de las sesiones
# Cada fila contiene: ID del cliente, duracion y numero de clics

sesiones = [
    [1001, 240, 12],
    [1002, 45, 5],
    [1003, 120, 6],
    [1004, 200, 2],
    [1005, 180, 9]
]


# Mostrar el informe de resultados
print("======================================")
print(" INFORME DE COMPROMISO DE CLIENTES")
print("======================================")
print("ID DEL CLIENTE     CLASIFICACION")
print("--------------------------------------")

# Recorrer la matriz y clasificar cada sesion
for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    resultado = clasificar_compromiso(duracion, clics)

    print(f"{id_cliente}              {resultado}")

print("--------------------------------------")
print("Proceso finalizado correctamente.")
