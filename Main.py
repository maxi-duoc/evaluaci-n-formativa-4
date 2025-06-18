import funciones as fc

opc = 0

while opc != 4:
    opc = fc.menu()

    match opc:
        case 1:
            pais = input('Ingrese el país: ').lower()
            fc.turistas_por_pais(pais)
        case 2:
            try:
                mes = int(input('Ingrese el mes (1-12): '))
                while mes < 1 or mes > 12 :
                    mes = int(input('Ingrese un mes válido (1-12): '))
                print(fc.turistas_por_mes(mes))
            except:
                print('Ingrese solo números enteros')
        case 3:
            fc.eliminar_turista()

print("Programa terminado...")