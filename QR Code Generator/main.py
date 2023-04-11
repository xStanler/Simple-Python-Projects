import qrcode
import os


def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=(89, 201, 111), back_color=(40, 40, 40))
    img.save(file_name)


directory = os.getcwd()
files = os.listdir(directory)

const_files = ['.idea', 'main.py']

for file in files:
    if not file in const_files:
        os.remove(os.path.join(directory, file))

# text = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
text = "xStanler on GitHub!"
file_name = 'qr.png'


generate_qr_code(text, file_name)
print("Done!")
