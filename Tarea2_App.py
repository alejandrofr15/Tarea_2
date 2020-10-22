from Tarea2_Finanzas import finanzas
from Tarea2_Ingresos import ingresos
from Tarea2_Egresos import egresos

x = finanzas()

while True:
    print("Menú de opciones:")
    print("0. Salir de la aplicación")
    print("1. Ver balance actual ")
    print("2. Agregar ingreso ")
    print("3. Agregar egreso ")
    print("4. Ver lista de ingresos ")
    print("5. Ver lista de egresos ")
    print("6. Ver lista de todas las transacciones")
    print("7. Ver suma de todos los ingresos")
    print("8. Ver suma de todos los egresos")
    print(" ")
    print(" ")

    option = int(input("Escribe el número de la opcion que desees realizar: "))

    if option == 0:
        print("Gracias por utilizar la aplicación")
        break

    elif option == 1:
        x.getSumTransacciones()
        print("___________________________________________________________")

    elif option == 2:
        x.AddIngreso()
        print("___________________________________________________________")

    elif option == 3:
        x.AddEgreso()
        print("___________________________________________________________")

    elif option == 4:
        x.getAllIngresos()
        print("___________________________________________________________")

    elif option == 5:
        x.getAllEgresos()
        print("___________________________________________________________")

    elif option == 6:
        x.getAllTransactions()
        print("___________________________________________________________")

    elif option == 7:
        x.getSumIngresos()
        print("___________________________________________________________")

    elif option == 8:
        x.getSumEgresos()
        print("___________________________________________________________")

    else:
        print('Has ingresado un número inválido. Vuelve a ingresar un número.')
        print("___________________________________________________________")

