import os
import pathlib
import shutil

def copiar_Arquivos(novaPasta, listadearquivos):
    #Create target Directory if don't exist
    if not os.path.exists(novaPasta):
        os.mkdir(novaPasta)

    caminhoAtual = str(pathlib.Path(__file__).parent.absolute())
    novaPasta = str(novaPasta)
    novocaminho = caminhoAtual + "\\" + novaPasta

    for iten in listadearquivos:
        shutil.copy(iten, novocaminho)

    return novocaminho