def carga_archivo_texto(archivo:str)->list:
    '''
    Carga un archivo de texto y devuelve una lista con las oraciones del archivo
    '''
 
    with open(archivo,'r') as file:
        oraciones = file.readlines()
    return oraciones
 
def carga_plantillas(nombre_plantilla:str)->dict:
    '''
    Carga las plantillas del juego a partir de un archivo de texto
    '''
    plantillas = {}
    for i in range(5):
        plantillas[i] = carga_archivo_texto(f'./Plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas
 
if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    carga_plantillas(plantilla, 0)