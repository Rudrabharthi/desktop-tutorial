import os
import shutil

path = input('Enter Path: ')
for entry in os.scandir(path):
    if entry.is_file():
        extension = os.path.splitext(entry.name)
        extension = extension[1:]  # Remove the dot from the extension

        destination_path = os.path.join(path, extension)
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        shutil.move(entry.path, os.path.join(destination_path, entry.name))