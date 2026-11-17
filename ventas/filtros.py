#parte de filtros: busca que paises cumplen una condicion y devuelve sus posiciones

def append_casero(lista: list, valor) -> list:
    '''
    es literalmente un append casero, recibev una lista y copia esa 
    lista de nuevo pero con un valor al final( no se modifica la lista original)
    por eso hay que reasignar
    
    args:
    lista(list): la lista original
    valor: el elemento que se quiere aggregar
    
    return:
    list: retorna la lista "nueva" con el elemento deseado al final
    '''
    nueva = [0] * ((len(lista)) + 1)
    for i in range(len(lista)):
        nueva[i] = lista[i]
    nueva[len(lista)] = valor
    return nueva


def buscar_indices(lista: list, limite: float, mayor: bool) -> list:
    '''
    recibe la lista, un limite y un mayor(true: busca mayores, False: menores)
    retorna la lista de posiciones que cumplen (vacia si ninguna)
    
    '''
    indices = []
    for i in range(len(lista)):
        if mayor and lista[i] > limite:
            indices = append_casero(indices, i)
        elif not mayor and lista[i] < limite:
            indices =  append_casero(indices, i)
    return indices


