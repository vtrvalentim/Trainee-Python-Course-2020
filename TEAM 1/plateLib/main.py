import searchPlates as sp
import readPlate as rp
import importaListaDeArquivos as ila
import pathlib

# Search for car imagens with license plate

sp.searchPlates()

# Lists all valid images

folder = pathlib.Path(__file__).parent.absolute()
targetFolder = "imagens_com_placa"
path= str(folder) + "\\" + str(targetFolder)

imagelist = ila.importFileList(path)

print("\nA lista de imagens carregadas é:")
for item in imagelist:
    print(item)

# Reads all plates

for item in imagelist:
    print(rp.readPlate(item))