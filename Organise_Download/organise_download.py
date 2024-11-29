import os
import shutil

def organise_folder(folder):
    file_types = {
        'Images': ['.jpeg', '.jpg', '.png'],
        'Archive': ['.zip', '.rar','.dmg', '.tar'],
        'Pdf\'s': ['.pdf', '.docx', '.txt', '.xlsx','.html'],
    }

    for file_name in os.listdir(folder):
        file_path =  os.path.join(folder, file_name)

        if not os.path.isfile(file_path):
            continue

        ext = os.path.splitext(file_name)[1].lower()
        for newFolder, extension in file_types.items():
            if ext in extension:
                move_to_folder = os.path.join(folder, newFolder)
                os.makedirs(move_to_folder, exist_ok=True)
                shutil.move(file_path, move_to_folder)
                print(f'Moved {file_path} to {move_to_folder}')
                break

organise_folder('/path/to/Downloads')
