
import requests
import os
import zipfile

os.chdir('/workspaces/PythonPC4/PC4/Problema3')

url = 'https://static.bandainamcoent.eu/high/dragon-ball/dragonball-project-z/00-page-setup/dbzk_game-thumbnail.jpg'

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64, x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

response = requests.get(url,headers=headers)

with open('DragonBallZ.jpg','wb') as f:
    f.write(response.content)
    pass

import zipfile


with zipfile.ZipFile('DragonBallZ.zip', 'w') as zip_file:
    zip_file.write('DragonBallZ.jpg')



#Crea carpeta
if not os.path.isdir('./descomprimir'): 
    os.mkdir('./descomprimir') 

#Extrae de archivos
with zipfile.ZipFile('DragonBallZ.zip', 'r') as zip_ref:
    zip_ref.extractall(path='./descomprimir')


    