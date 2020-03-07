import googleObjectDetect
import importaListaDeArquivos
import copiaArquivosParaNovaPasta
import pathlib

#CaminhoInicial
#A pasta deve estar na mesma pasta do script e deve se chamar "imagens"
#dentro dessa pasta devem ser colocados arquivos com extensões de imagem
def searchPlates():
    pasta = pathlib.Path(__file__).parent.absolute()
    pastaImagens = "imagens"
    caminho = str(pasta) + "\\" + str(pastaImagens)

    imagelist = importaListaDeArquivos.importFileList(caminho)

    print("\nA lista de imagens carregadas é:")
    for iten in imagelist:
        print(iten)

    print("\nAguarde: o Google vision irá identificar as imagens que possuem uma license plate...")

    imagelistLicensePlate = list()

    licensePlate = "License plate"

    #Neste trecho é feita a leitura de objetos na imagem e a criação da lista de imagens que tem uma placa
    for iten in imagelist:
        objetos = googleObjectDetect.localize_objects(iten)
        if (licensePlate in objetos):
            imagelistLicensePlate.append(iten)

    print("\nAs imagens que possuem uma license plate são:")
    for iten in imagelistLicensePlate:
        print(iten)

    #Neste Trecho os arquivos são salvos na nova pasta

    novaPasta = "imagens_com_placa"
    novoCaminho = copiaArquivosParaNovaPasta.copiar_Arquivos(novaPasta,imagelistLicensePlate)

    print("Os arquivos foram salvos na pasta: ",str(novoCaminho))