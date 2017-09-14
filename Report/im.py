from os import system
from os import path
from os import listdir

IMG_DIR = './Images/'

EXT_OLD = '.jpg'
EXT_NEW = '.png'

file_list = []

for file in listdir(IMG_DIR):
    if file.endswith(EXT_OLD):
        file_list.append(path.join(IMG_DIR, file))

for file_name in file_list:
    print('Converting: ' + file_name)
    file_new_name = file_name[:-3] + EXT_NEW
    print(file_name)
    print(file_new_name)
    system('convert ' + file_name + ' ' + file_new_name)
    system('rm ' + file_name)