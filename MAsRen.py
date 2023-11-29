import os
import time
from art import tprint
tprint ('MAsRen V1.0')
print('GitHub > https://github.com/ErkinKraft')
time.sleep(3)
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')


def change_extension_double():
    folder_path = input("Введите путь к папке> ")
    old_extension = input("Введите первое расширение файлов (без точки)> ")
    new_extension = input("Введите новое расширение файлов (без точки)> ")

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(f".{old_extension}"):
                file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file.replace(f".{old_extension}", f".{new_extension}"))
                os.rename(file_path, new_file_path)

    print("Расширение файлов успешно изменено!")

    allow = input('Ещё? (y/n)> ')
    if allow == 'y':
        change_extension_double()
    else:
        tprint('Goodbay')
        time.sleep(2)
        exit(1)

change_extension_double()



