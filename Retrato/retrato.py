from PIL import Image

# Mapa de caracteres ASCII (se recomienda tener más caracteres para una mejor representación)
ASCII_CHARS = "@%#!+*-:. "  # Asegúrate de que haya 10 caracteres

def resize_image(image, new_width=130):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    factor = 0.4  # O el valor que desees
    new_height = int(aspect_ratio * new_width * factor)
  # Ajustamos la altura sin dividir por 2
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")  # Convierte a escala de grises

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // (264 // len(ASCII_CHARS))]  # Mapea el pixel a un carácter ASCII
    return ascii_str

def image_to_ascii(image_path, new_width=130):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width

    # Divide la cadena ASCII en líneas de ancho de imagen
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join(ascii_str[i:i + img_width] for i in range(0, ascii_str_len, img_width))

    return ascii_img

# Ruta de la imagen
image_path = "img/persona.jpg"  # Cambia esto por la ruta a tu imagen
ascii_art = image_to_ascii(image_path)

if ascii_art:
    # Imprimir el arte ASCII
    print(ascii_art)
