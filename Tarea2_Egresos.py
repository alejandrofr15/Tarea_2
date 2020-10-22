class egresos:
    def __init__(self):
        self.__listaEgresos = []

    def AddEgreso(self, descripcion, monto):
        dicc = {'Descripcion': descripcion, 'Monto': (-1)*(float(monto))}
        self.__listaEgresos.append(dicc)


    def getAllEgresos(self):
        return self.__listaEgresos

    def getSumEgresos(self):
        suma = 0
        for x in self.__listaEgresos:
            suma = suma + float(x['Monto'])
        return suma


