#Parte encargada de los calculos del programa

def suma_de_lista(lista: list) -> int:
    '''
    vendria siendo una sum casera masomenos, suma los elementos de una lista
    
    args:
    recibe la lista con los elementos a sumar

    return:
    retorna un entero con los elemetos de la lista sumados
    
    '''
    resultado = 0
    for i in range(len(lista)):
        resultado += lista[i]
    return resultado

def promedio_de_lista(lista: list) -> float: 
    '''
    calcula el promedio de la lista: se suma todo yt se dividie por la 
    cantidad de elementos de la lista

    args:
    lista(list): lista de numeros

    return:
    float: devuelve el promedio, es un float porque da con coma decimal 
    
    '''

    resultado = 0 
    if len(lista) > 0:
        resultado = suma_de_lista(lista) / len(lista)
    return resultado


def maximo_de_lista(lista: list) -> int:
    '''
    Recibe una lista de numeros. Retorna el maximo o mayor valor de esta
    o 0 si esta vacia

    args:
    lista(list): lista a evaluar el maximo

    return:
    retorna el numero que era el mayor de la lista
    
    '''
    resultado = 0
    if len(lista) > 0:
        resultado = lista[0]
        for i in range(1, len(lista)):
            if lista[i] > resultado:
                resultado = lista[i]
    return resultado

def calculador_porcentaje(parte: int, total: int) -> float:
    '''
    recibe por parametro una parte y un total, retorna que porcentaje del total
    es la parte o retorna 0 si el total es 0
    '''
    resultado = 0
    if total > 0:
        resultado = parte * 100 / total
    return resultado




