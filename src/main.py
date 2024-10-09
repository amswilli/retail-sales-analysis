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
    
    datos_sin_ceros = eliminar_columnas_con_ceros(datos)
    
    datos_relevantes = seleccionar_columnas_relevantes(datos_sin_ceros)
    
    datos_limpios = normalizar_columnas_relevantes(datos_relevantes)
    
    #Mostrar los primeros 5 registros
    print("Primeros 5 registros:")
    print(
        datos_limpios[:5]
    )