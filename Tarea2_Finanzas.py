from Tarea2_Ingresos import ingresos
from Tarea2_Egresos import egresos

class finanzas():
    def __init__(self):
        self.ListaTransacciones = []
        self.obj = ingresos()
        self.cosa = egresos()
    

    def getAllTransactions (self):
        for vari in self.ListaTransacciones:
            print(vari)

    def getAllIngresos(self):
        print("Estos son todos los ingresos registrados hasta ahora:")
        lista = self.obj.getAllIngresos()
        for itera in lista:
            print(itera)
        

    def getAllEgresos(self):
        print("Estos son todos los egresos registrados hasta ahora:")
        lista2 = self.cosa.getAllEgresos()
        for iterad in lista2:
            print(iterad)

    def AddIngreso(self):
        print('Ingresarás un nuevo ingreso. Escribe los datos correspondientes:')
        descripcion = input("Descripción: ")
        monto = float(input("Monto:"))
        Transaccion = {'Descripción': descripcion, 'Monto': float(monto)}
        self.obj.AddIngreso(descripcion, monto)
        self.ListaTransacciones.append(Transaccion)

    def AddEgreso(self):
        print('Ingresarás un nuevo egreso. Escribe los datos correspondientes:')
        descripcion = input("Descripción: ")
        monto = float(input("Monto:"))
        self.cosa.AddEgreso(descripcion, monto)
        Transaction = {'Descripción': descripcion, 'Monto': float((-1)*(monto))}
        self.ListaTransacciones.append(Transaction)

    def getSumIngresos(self):
        print("Esta es la suma de todos los ingresos registrados hasta ahora")
        suma = float(self.obj.getSumIngresos())
        print(suma)

    def getSumEgresos(self):
        print("Esta es la suma de todos los egresos registrados hasta ahora")
        suma = float(self.cosa.getSumEgresos())
        print(suma)

    def getSumTransacciones(self):
        suma = 0
        for x in self.ListaTransacciones:
            suma = suma + float(x['Monto'])
        print('Este es el balance de tu cuenta:' + str(suma))
        

