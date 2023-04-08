import os
from datetime import datetime
import shutil

directory = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive\Pulpit')
print(directory)

file_extensions = {
    'url': "Shortcuts",
    'odt': 'Documents',
    'txt': 'Documents',
    'lnk': 'Shortcuts',
    'xcf': 'Graphics',
    'docx': 'Documents',
    'pptx': 'Documents',
    'png': 'Graphics',
    'jpg': 'Graphics'
}

folders = ['Shortcuts', 'Documents', 'Graphics', 'Other']

files = os.listdir(directory)
print(files)

for folder in folders:
    if not folder in files:
        os.mkdir(os.path.join(directory, folder))

# for folder in folders:
#     os.rmdir(os.path.join(directory, folder))

print("Done")

for file in files:
    # time = os.path.getctime(os.path.join(directory, file)) # getting time of file creatrion (WINDOWS only)
    # date = datetime.fromtimestamp(time) # converting timestamp to proper date

    if os.path.isfile(os.path.join(directory, file)):
        file_arr = file.split('.')
        ext = file_arr[-1]

        destinationFolder = file_extensions.get(ext)
        if destinationFolder != None:
            shutil.move(os.path.join(directory, file), os.path.join(directory, destinationFolder, file))
        else:
            shutil.move(os.path.join(directory, file), os.path.join(directory, 'Other', file))
    elif not file in folders:
        shutil.move(os.path.join(directory, file), os.path.join(directory, 'Other', file))