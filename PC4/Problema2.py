from pyfiglet import Figlet
import random

def mostrar_figlet(texto, fuente):

    figlet = Figlet()
    json_figlet = figlet.getFonts() ##obtenemos el json
    numero_random = int(len(json_figlet)*random.random()) ##obtenemos un número random

    if fuente == '': ##si no arroja nada, entonces uno random
        figlet.setFont(font=json_figlet[numero_random])
    else: ##si hay data entonces que muestre
        figlet.setFont(font=fuente)

    texto_final = figlet.renderText(texto)

    return print(texto_final)

    pass

texto = input('Digite un texto: ')
fuente = input('Digite una fuente para el texto: ')

print(mostrar_figlet(texto,fuente))