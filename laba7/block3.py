import os
import shutil
import subprocess

def open_file(file_path: str):
    """Открывает файл текстовым редактором."""
    try:
        subprocess.run(["notepad", file_path], check=True)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")

def create_file_or_folder(path: str, is_folder: bool = False):
    """Создает файл или папку."""
    try:
        if is_folder:
            os.makedirs(path, exist_ok=True)
            print(f"Папка {path} успешно создана.")
        else:
            with open(path, 'w') as file:
                file.write("")
            print(f"Файл {path} успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании: {e}")

def rename_file_or_folder(old_path: str, new_path: str):
    """Переименовывает файл или папку."""
    try:
        os.rename(old_path, new_path)
        print(f"{old_path} переименован(а) в {new_path}.")
    except FileNotFoundError:
        print(f"Файл или папка {old_path} не найдены.")
    except Exception as e:
        print(f"Ошибка при переименовании: {e}")


if __name__ == "__main__":
    #1
    file_to_open = "example.txt"  # Замените на имя файла
    open_file(file_to_open)

    #5
    new_file_path = "new_file.txt"  # Замените на путь и имя
    create_file_or_folder(new_file_path)

    
    new_folder_path = "new_folder"  # Замените на путь и имя
    create_file_or_folder(new_folder_path, is_folder=True)

    #7
    old_name = "old_file.txt"  # Замените на текущее имя
    new_name = "renamed_file.txt"  # Замените на новое имя
    rename_file_or_folder(old_name, new_name)
