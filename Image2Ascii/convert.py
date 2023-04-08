from PIL import Image
import os

def color2acii(r, g, b):
    ascii_scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"'. "

    brightness = (r + g + b) / 3
    scale_factor = round(255 / len(ascii_scale))
    index = round(brightness / scale_factor)
    return ascii_scale[index]

def convert(file):
    with Image.open(f"Photos/{file}") as im:
        width, height = im.size

        text_im = ''
        for h in range(height):
            row = ''
            for w in range(width):
                r, g, b = im.getpixel((w, h))
                char = color2acii(r, g, b)
                row += char
            text_im += row + '\n'

    name = file.split('.')[0]
    with open(f'Output/{name}.txt', 'w') as output:
        output.writelines(text_im)

print("Remember that in Photo folder there must be only images with '.jpg' extension!!!")

directory = os.path.join(os.getcwd(), 'Photos')

photos = os.listdir(directory)

for photo in photos:
    print(photo)
    convert(photo)
    print(f"Converting {photo} - done!")
