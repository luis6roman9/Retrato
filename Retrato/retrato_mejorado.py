from PIL import Image
import numpy as np


def imagen_a_ascii(ruta_imagen, ancho = 900):
    # Abrir la imagen
    imagen = Image.open(ruta_imagen)

    # Calcular la altura proporcional para mantener la relación de aspecto
    proporcion = imagen.height / imagen.width * 0.45 
    altura = int(ancho * proporcion)

    # Redimensionar la imagen
    imagen = imagen.resize((ancho, altura))

    # Convertir la imagen a escala de grises
    imagen_grises = imagen.convert("L")

    # Definir caracteres ASCII a utilizar
    caracteres = "@%#*+=-"
    
    num_caracteres = len(caracteres)

    # Crear un array numpy a partir de la imagen
    datos = np.array(imagen_grises)

    # Mapear los valores de píxeles a caracteres ASCII
    ascii_map = (datos / 250 * (num_caracteres - 1)).astype(int)

    # Crear la representación ASCII
    ascii_imagen = ""
    for fila in ascii_map:
        for valor in fila:
            ascii_imagen += caracteres[valor]
        ascii_imagen += "\n"

    return ascii_imagen


# Ruta de la imagen a convertir
ruta_imagen = 'img/persona.jpg'  # Cambia esto por la ruta de tu imagen

# Generar el mapa ASCII
ascii_art = imagen_a_ascii(ruta_imagen)

# Guardar el resultado en un archivo
with open('imagen.txt', 'w') as f:
    f.write(ascii_art)

print("Mapa de caracteres ASCII generado y guardado en 'imagen.txt'")
