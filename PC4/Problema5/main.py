
from Problema5 import *

MENU = """
1. Guardar fichero en .txt
2. Recuperar fichero en .txt
3. Leer línea del fichero en .txt
4. Salir.
"""

def main():
    print('Bienvenido a la tabla de multiplicar')
    
    while(True):
        opc = int(input(MENU))
        if opc == 1:
            guardar_tabla_multiplicar()
            pass
        elif opc == 2:
            recuperar_archivo(get_int('Ingrese un número entre 1 y 10: '))
            pass
        elif opc == 3:
            linea = int(input('Ingrese la línea a recuperar: '))
            recuperar_linea_archivo(get_int('Ingrese el número de archivo .txt recuperar: '),linea)
            pass
        elif opc == 4:
            print('Saliendo del programa.')
            break
        else:
            break
        pass
    pass

if __name__ == '__main__':
    main()