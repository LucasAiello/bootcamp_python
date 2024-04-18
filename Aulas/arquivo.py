import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    file_2 = open("eita.txt")
except FileNotFoundError as exc:
    print("Nao encontrado")
    print(exc)


try:
    os.mkdir(ROOT_PATH / 'pasta')
except:
    ...

try:
    os.remove(ROOT_PATH / 'pasta')
except PermissionError:
    print("Plim")
# os.rename() 
#file = open("arquivo.txt", 'r') # ler arquivo
# escrever um arquivo
#file = open("arquivo.txt", 'a') # colocar mais conteudo no arquivo

"""
while len(linha := file.readline()):
    print(linha)

#print(file.read())
#print(file.readlines())
"""

try:
    with open("arquivo.txt", 'w', encoding="utf-8") as file:

        file.write("Eitaaaaa")
        file.writelines("\nPychon")
        file.writelines(["Estou\n", "Escrevendo???"])
except IOError as exc:
    print(exc)


#file.close()