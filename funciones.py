turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

def menu():
    print('''
*** MENU PRINCIPAL ***
1.- Turistas por país.
2.- Turista por mes.
3.- Eliminar turista.
4.- Salir''')
    return int(input('Ingrese una opción: '))
    
def turistas_por_pais(pais):

    # Evita que sean ingresados digitos
    if pais.isnumeric():
        print('Ingrese un país válido')
        return


    existe = False # Para ver si hubo un turista

    # Busca por cada lista el pais dado
    for clave, valor in turistas.items():
        if valor[1].lower() == pais:
            existe = True
            print(turistas[clave])
    
    # Si no encontró ningún turista
    if not existe:
        print('No se ha encontrado a ningún turista de ese país')

def turistas_por_mes(mes):
    # Variables para el calculo
    turistasEnElMes= 0
    total = 0

    # Suma cada turista de ese mes y tambien suma a todos al total
    for valor in turistas.values():
        if int(valor[2][3:5]) == mes:
            turistasEnElMes += 1
        total += 1
    
    # Calcula el porcentaje de ese mes
    porcentajePorMes = round(turistasEnElMes / total * 100)

    return f"El porcentaje de turistas de ese mes es de: {porcentajePorMes}%"

def eliminar_turista():

    existe = False
    nombre = input('Ingrese el nombre del turista que desea eliminar: ').lower()

    # Itera cada lista del diccionario en busca del nombre dado
    for clave, valor in turistas.items():
        if valor[0].lower() == nombre:
            existe = True
            print(f"El turista llamado {valor[0]} ha sido eliminado")
            del turistas[clave]
            return
    
    if not existe:
        print('No se ha encontrado a ningún turista de ese nombre')

