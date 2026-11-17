from ventas.calculos import suma_de_lista, calculador_porcentaje, maximo_de_lista

def mostrar_ventas(lista: list) -> None:
    '''
    Recibe las ventas y muestra cada region con su cantidad y porcentaje y el total

    args:
    lista(list): lista de ventas

    return: 
    no retorna nada
    
    '''
    total = suma_de_lista(lista)
    for i in range(len(lista)):
        porcentaje = calculador_porcentaje(lista[i], total)
        print(f"region {i + 1}: {lista[i]} productos ({porcentaje:.2f}%)")
    print(f"Total de productos vendidos: {total}")

def mostrar_resultados(lista: list, indices: list) -> None:
    '''
    recibe las ventas y los indices de las ventas, muestra la
    informacion de cada region con su cantidad y porcenytaje y el total, etc

    
    '''
    total = suma_de_lista(lista)
    if len(indices) == 0:
        print("Error: ninguna region cumple con la condicion")
    else:
        suma = 0
        for i in range(len(indices)):
            valor = lista[indices[i]]
            porcentaje = calculador_porcentaje(valor, total)
            print(f"Region {indices[i] + 1}: {valor} productos ({porcentaje:.2f}%)")
            suma += valor
        print(f"suma de ventas: {suma}")
        print(f"cantidad de regiones: {len(indices)}")
        print(f"promedio de ventas: {suma / len(indices):.2f}")
        print(f"porcentaje acumulado: {calculador_porcentaje(suma, total):.2f}%")

def mostrar_mas_compradores(lista: list) -> None:
    ''''
    Recibe las ventas. Muestra la region con mas ventas(todas las empatadas)
    '''
    total = suma_de_lista(lista)
    mayor = maximo_de_lista(lista)
    for i in range(len(lista)):
        if lista[i] == mayor:
            porcentaje = calculador_porcentaje(lista[i], total)
            print(f"Region {i + 1}: {lista[i]} productos ({porcentaje:.2f}%)")

