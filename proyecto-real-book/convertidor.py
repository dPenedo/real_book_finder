import json

def convertir_a_json(archivo_entrada, archivo_salida):
    # Leer el archivo de texto y dividir las líneas en bloques de nombre e índice
    with open(archivo_entrada, 'r') as file:
        lineas = file.readlines()

    data = {"canciones": []}
    cancion_actual = None

    for linea in lineas:
        linea = linea.strip()
        if linea.isdigit():
            # Es un índice
            if cancion_actual:
                cancion_actual["indice"] = int(linea)
                data["canciones"].append(cancion_actual)
        elif linea:
            # Es el nombre de una canción
            cancion_actual = {"nombre": linea}

    # Guardar en formato JSON
    with open(archivo_salida, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

# Llamar a la función con el nombre del archivo de entrada y salida
convertir_a_json('indice3_sl.txt', 'real-book-3.json')

