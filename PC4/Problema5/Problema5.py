
import os

##Me dirigo a la ruta del Problema5
os.chdir('/workspaces/PythonPC4/PC4/Problema5')

def get_int(msg:str)->int:
    try:
        x = int(input(msg))
        assert x>=1 and x<=10, 'Numero debe estar entre 1 y 10'
        return x 
    except:
        print('Dato erroneo, vuelva a intentar ...')
        return get_int(msg)
    


def guardar_tabla_multiplicar():
    # Solicitar un número entero entre 1 y 10
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")
    
    # Generar y guardar la tabla de multiplicar en el fichero tabla-n.txt
    with open(f'./tabla-{n}.txt', 'w') as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n * i}\n")

    print(f"La tabla de multiplicar del {n} se ha guardado en ./src/tabla-{n}.txt")



def recuperar_archivo(n:int):
    """Recupera fichero de la tabla de multiplicar"""
    try:
        ruta_archivo = f'./tabla-{n}.txt'
        data = open(ruta_archivo, mode='r').read()
        print(data)
    except FileNotFoundError:
        print('Archivo no encontrado ...')
    pass

def recuperar_linea_archivo(n:int,m:int):
    """Recupera fichero de la tabla de multiplicar"""
    try:
        ruta_archivo = f'./tabla-{n}.txt'
        data = open(ruta_archivo, mode='r')
        lineas = data.readlines()
        if len(lineas) >= m:
            print(lineas[m - 1])
        else:
            print("La línea especificada no existe en el archivo.")

    except FileNotFoundError:
        print('Archivo no encontrado ...')
    pass


if __name__ == '__main__':
    #guardar_tabla_multiplicar()
    #recuperar_archivo(get_int('Ingrese un número del 1 al 10: '))
    #linea = int(input('Ingrese la línea a recuperar: '))
    #recuperar_linea_archivo(get_int('Ingrese un número del 1 al 10: '),linea)
    pass