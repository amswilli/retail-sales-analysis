import numpy as np

def cargar_datos(ruta_archivo):
    try:
        datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1)
        return datos
    except FileNotFoundError:
        print(f"El archivo no se encontró: {ruta_archivo}")
        return None

if __name__ == "__main__":
    ruta_archivo = "../data/retail_sales_dataset.csv"
    #Cargar los datos
    datos = cargar_datos(ruta_archivo)
    if datos is not None:
        print(datos)