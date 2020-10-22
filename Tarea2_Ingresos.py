class ingresos:
    def __init__(self):
        self.__listaIngresos = []

    def AddIngreso(self, descripcion, monto):
        dicc = {'Descripcion': descripcion, 'Monto': monto}
        self.__listaIngresos.append(dicc)

    def getAllIngresos(self):
        return self.__listaIngresos

    def getSumIngresos(self):
        suma = 0
        for x in self.__listaIngresos:
            suma = suma + float(x['Monto'])
        return suma


