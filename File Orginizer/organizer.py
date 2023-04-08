import os
import shutil

extension_groups = {
    'jpg': 'Graphics',
    'png': 'Graphics',
    'jpeg': 'Graphics',
    'txt': 'Documents',
    'docx': 'Documents',
    'dot': 'Documents',
    'doc': 'Documents',
    'pptx': 'Documents',
    'lnk': 'Shortcuts',
    'url': 'Shortcuts'
}

folders = ['Graphics', 'Documents', 'Shortcuts', 'Other']

directory = os.path.join(os.environ['USERPROFILE'], 'OneDrive\Pulpit')
files = os.listdir(directory)

for folder in folders:
    if folder not in files:
        os.mkdir(os.path.join(directory, folder))

for file in files:
    if os.path.isfile(os.path.join(directory, file)):
        ext = file.split('.')[-1]
        destination_name = extension_groups.get(ext)
        destination_dir = os.path.join(directory, destination_name)

        if destination_name != None:
            shutil.move(os.path.join(directory, file), os.path.join(destination_dir, file))
        else:
            shutil.move(os.path.join(directory, file), os.path.join(directory, 'Other', file))
    elif file not in folders:
        shutil.move(os.path.join(directory, file), os.path.join(directory, 'Other', file))