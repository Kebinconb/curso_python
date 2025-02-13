'''
Programa principal del juego del ahoracado
'''
import string
import funciones as fn
from random import choice

def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''
    Programa principal
    '''
    #Cargamos las plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)
    lista_oraciones = fn.carga_archivo_texto(archivo_texto)
    palabras = fn.obten_palabras(lista_oraciones)
    o = 5 #oportunidades
    p = choice(palabras)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o > 1:
        fn.despliega_plantilla(plantillas, o)
        fn.adivina_letra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Ganaste')
            break
    o -= 1