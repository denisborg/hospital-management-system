class Configuracoes():
    def __init__(self):
        self.__file_pacientes = './bancos/pacientes.csv'
        self.__file_consultas = './bancos/consultas.csv'
        self.__file_procedimentos = './bancos/procedimentos.csv'
        self.__file_logs = './logs/log.txt'
    
    @property
    def file_pacientes(self):
        return self.__file_pacientes
    
    @property
    def file_consultas(self):
        return self.__file_consultas

    @property
    def file_procedimentos(self):
        return self.__file_procedimentos

    @property
    def file_logs(self):
        return self.__file_logs