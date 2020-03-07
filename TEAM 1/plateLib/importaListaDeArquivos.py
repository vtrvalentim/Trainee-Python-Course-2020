import os
def importFileList(path):
    # __________________________________________________________________________________________________________________
    # DESCRICAO
    # Essa funcao carrega uma lista com o nome de todos os arquivos presentes em uma pasta, dado um caminho fornecido
    # A funcao retorna a lista contendo os caminhos de cada arquivo
    # __________________________________________________________________________________________________________________

    lista_iterada = os.scandir(path)

    filelist = list()

    for iten in lista_iterada:
        filelist.append(iten.path)

    return filelist