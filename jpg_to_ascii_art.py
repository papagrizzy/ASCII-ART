from PIL import Image


character_key_set = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def pixel_to_char_converter(pixel):
    (r, g, b) = pixel
    luminosity = r + g + b
    luminosity_max = 255 * 3
    luminosity_leverage = len(character_key_set) / luminosity_max
    position = int(luminosity * luminosity_leverage) - 1
    return character_key_set[position]


def basic_ascii_config(image):
    converted = []
    (width, height) = image.size
    for i in range(height - 1):
        lit = ""
        for j in range(width - 1):
            pixel = image.getpixel((j, i))
            lit += pixel_to_char_converter(pixel)
        converted.append(lit)
    return converted


def stockpile(converted):
    with open("ascii_art.txt", "w") as file:
        for lit in converted:
            file.write(lit)
            file.write('\n')
        file.close()


def main():
    image = Image.open('sample.jpg')
    converted = basic_ascii_config(image)
    stockpile(converted)


if __name__ == '__main__':
    main()

