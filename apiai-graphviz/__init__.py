import zipfile as zp

''' 
1. Extrair zip
2. abrir dir intents
3. parse all jsons to memory
4. remove unwanted info
5. build graph object for each intent
6. get connections
'''


def unzip():
    with zp.ZipFile("../Aquamote-EN.zip","r") as zip_ref:
        zip_ref.extractall("aquamote")

