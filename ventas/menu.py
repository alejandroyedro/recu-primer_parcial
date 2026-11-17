from ventas.entrada import pedir_opcion, carga_secuencial
from ventas.calculos import suma_de_lista, promedio_de_lista
from ventas.filtros import buscar_indices
from ventas.reportes import mostrar_mas_compradores, mostrar_resultados, mostrar_ventas



CANTIDAD_REGIONES = 6


def mostrar_menu() -> None:
    """No recibe nada. Imprime las opciones del menu. No retorna nada."""
    print("\n[1] CARGAR VENTAS")
    print("[2] MOSTRAR VENTAS")
    print("[3] REGIONES CON MENOS DEL 5% DE LAS VENTAS")
    print("[4] REGIONES CON MENOS DEL 25% DE LAS VENTAS")
    print("[5] REGIONES CON MAS DE 500 VENTAS")
    print("[6] REGIONES CON MAS DE 3000 VENTAS")
    print("[7] REGIONES POR ENCIMA DEL PROMEDIO")
    print("[8] REGION/ES MAS COMPRADORA/S")
    print("[0] SALIR")


def ejecutar_menu() -> None:
    """No recibe nada. Repite el menu hasta salir y bloquea las opciones 2 a 8 hasta cargar datos."""
    ventas = []
    hay_datos = False
    salir = False
    while not salir:
        mostrar_menu()
        opcion = pedir_opcion(0, 8)
        if opcion == 0:
            print("Chau")
            salir = True
        elif opcion == 1:
            ventas = carga_secuencial(CANTIDAD_REGIONES)
            hay_datos = True
        elif hay_datos == False:
            print("Error: primero tenes que cargar las ventas (opcion 1).")
        elif opcion == 2:
            mostrar_ventas(ventas)
        elif opcion == 3:
            mostrar_resultados(ventas, buscar_indices(ventas, suma_de_lista(ventas) * 5 / 100, False))
        elif opcion == 4:
            mostrar_resultados(ventas, buscar_indices(ventas, suma_de_lista(ventas) * 25 / 100, False))
        elif opcion == 5:
            mostrar_resultados(ventas, buscar_indices(ventas, 500, True))
        elif opcion == 6:
            mostrar_resultados(ventas, buscar_indices(ventas, 3000, True))
        elif opcion == 7:
            promedio = promedio_de_lista(ventas)
            print(f"Promedio general: {promedio:.2f}")
            mostrar_resultados(ventas, buscar_indices(ventas, promedio, True))
        elif opcion == 8:
            mostrar_mas_compradores(ventas)
