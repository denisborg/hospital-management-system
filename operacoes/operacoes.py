from persistir.persistir import Persistir

class Operacao():
    def __init__(self):
        self.__persistir = Persistir()

    def Pacientes(self, option, nome=None, cpf=None, data_nasc=None):
        self.__option = option
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nasc = data_nasc

    def save(self):
        self.__persistir.wrote_file(
            self.__option, self.__nome, self.__cpf, self.__data_nasc    
        )