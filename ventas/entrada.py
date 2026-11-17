#Parte encargada de la validacion de datos para evitar que se rompa el programa

def es_entero_positivo(texto: str, ) -> bool:
    '''
    Valida que los datos que carguemos sean digitos(numeros) y que sea mayor que 0(que no este vacio)

    args: digitos a evaluar(numeros)

    retunr un booleano true en caso de todos los caracteres sean digitos y en caso de que no, retorna un false
    '''
    es_valido = True
    if len(texto) == 0:
        es_valido = False
    else:
        for i in range(len(texto)):
            if ord(texto[i]) < 48 or ord(texto[i]) > 57:
                es_valido = False
    return es_valido


# print(es_entero_positivo())

def convertir_a_entero(texto: str) -> int:
    '''
    convierte un texto de digitos(str) en un numero(pasa el numero que escribis de str a int)

    args:
    texto(str): recibe un texto formado solo por digitos

    return:
    int: el numero que queria representar
    
    '''
    numero = 0 
    for i in range(len(texto)):
        numero =  numero * 10 + (ord(texto[i]) - 48)
    return numero

def pedir_entero_positivo(mensaje: str) -> int:
    '''
    pide un dato por teclado y repite la pregunta hasta que sea un entero mayor que cero

    args:
    mensaje(str): el texto que se muestra al pedi el dato

    return:
    int: el numero ya convertido

    '''
    numero = 0 
    es_valido = False
    while not es_valido:
        dato = input(mensaje)
        if es_entero_positivo(dato) == False:
            print("Error. Ingrese solo numero enteros")
        else:
            numero = convertir_a_entero(dato)
            if numero > 0:
                es_valido = True
            else:
                print("Error. El numero debe ser mayor a 0")
    return numero

def carga_secuencial(cantidad: int) -> list:
    '''
    carga secuencialmente en una lista, posicion por posicio
    
    args:
    cantidad(int): cuantos datos hay que cargar

    return:
    list: lista con la cantidad cargada
    
    '''

    lista = [0] * cantidad
    for i in range(len(lista)):
        lista[i] = pedir_entero_positivo(f"Region {i + 1}: ")
    return lista

def pedir_opcion(desde: int, hasta: int) -> int:
    '''
    basicamente pide la opcion del menu y repite hasta que sea un 
    numero entero permitido en las opciones (1 y 10)
    
    args:
    desde(int): opcion minima (1) 
    hasta(int): opcion maxima valida (10)

    return:
    int: la opcion elegida
    '''

    opcion = 0
    es_valido = False
    while not es_valido:
        texto = input("elija una opcion: ")
        if es_entero_positivo(texto) ==  False:
            print("Eror. Ingrese solo numeros")
        else:
            opcion = convertir_a_entero(texto)
            if opcion >= desde and opcion <= hasta:
                es_valido = True
            else:
                print(f"Eror. la oopcion debe estar entre {desde} y {hasta}")
    return opcion

