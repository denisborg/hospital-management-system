import csv

from configs.configs import Configuracoes
from datetime import date

class Persistir():
    def __init__(self):
        self.__configurations = Configuracoes()

    def wrote_file(self, option, nome, cpf, data_nasc):
        if option == '1':
            registro_paciente = [nome, cpf, data_nasc]
            with open(self.__configurations.file_pacientes, 'a', newline='', encoding='UTF-8') as arquivo:
                escritor = csv.writer(arquivo, delimiter=',')
                escritor.writerow(registro_paciente)