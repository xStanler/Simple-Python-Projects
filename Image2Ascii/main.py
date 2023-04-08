from PIL import Image
from math import floor
import os

def colorToAscii(bright):
    ascii_palette = "$@B%7&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"'.                "
    ascii_factor = 255 /len(ascii_palette)
    index = len(ascii_palette) - round(bright/ascii_factor) - 1
    return ascii_palette[index]

def convert_img(file):
    im = Image.open(f"Photos/{file}.jpg")

    width, height = im.size

    img_ascii = ''
    for h in range(height):
        row = ''
        for w in range(width):
            r, g, b = im.getpixel((w, h))
            brightness = floor((r + g + b) / 3)
            row += colorToAscii(brightness)
        img_ascii += row + '\n'

    with open(f'{file}.txt', 'w') as output:
        output.writelines(img_ascii)

print("Remember images must be in jpg format!")

photo_dir = os.path.join(os.getcwd(), 'Photos')
photos = os.listdir(photo_dir)

for photo in photos:
    name, ext = photo.split('.')

    convert_img(name)

print("All done!")
