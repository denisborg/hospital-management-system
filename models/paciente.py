import os
import pandas as pd
from utils.configs import Configuracoes
from utils.log import registrar_log

class Paciente:
    def __init__(self):
        self.__configurations = Configuracoes()
        self.arquivo_csv = self.__configurations.file_pacientes
        self.arquivo_id  = self.__configurations.file_ult_id_paciente

        # Criar arquivo CSV se não existir
        if not os.path.exists(self.arquivo_csv):
            df = pd.DataFrame(columns=['id', 'nome', 'cpf', 'data_nasc', 'sexo'])
            df.to_csv(self.arquivo_csv, index=False)

        # Criar arquivo de ID se não existir ou estiver vazio
        if not os.path.exists(self.arquivo_id) or os.path.getsize(self.arquivo_id) == 0:
            with open(self.arquivo_id, 'w') as f:
                f.write('0')

    def gerar_novo_id(self):
        with open(self.arquivo_id, 'r') as f:
            conteudo = f.read().strip()
            ultimo_id = int(conteudo) if conteudo else 0

        novo_id = ultimo_id + 1
        with open(self.arquivo_id, 'w') as f:
            f.write(str(novo_id))
        return novo_id

    def cadastrar_paciente(self, nome, cpf, data_nasc, sexo):
        id = self.gerar_novo_id()
        df = pd.read_csv(self.arquivo_csv)
        df.loc[len(df.index)] = [id, nome, cpf, data_nasc, sexo]
        df.to_csv(self.arquivo_csv, index=False)
        registrar_log(f"PACIENTE CADASTRADO: ID={id}, Nome={nome}, CPF={cpf}")

    def listar_pacientes(self):
        df = pd.read_csv(self.arquivo_csv)
        return df

    def buscar_paciente_por_id(self, id):
        df = pd.read_csv(self.arquivo_csv)
        paciente = df[df['id'] == id]
        if not paciente.empty:
            return paciente.iloc[0].to_dict()
        return None

    def editar_paciente(self, id, nome, cpf, data_nasc, sexo):
        df = pd.read_csv(self.arquivo_csv)
        if id in df['id'].values:
            df.loc[df['id'] == id, ['nome', 'cpf', 'data_nasc', 'sexo']] = [nome, cpf, data_nasc, sexo]
            df.to_csv(self.arquivo_csv, index=False)
            registrar_log(f"PACIENTE EDITADO: ID={id}, Nome={nome}, CPF={cpf}")
            return True
        return False

    def excluir_paciente(self, id):
        df = pd.read_csv(self.arquivo_csv)
        if id in df['id'].values:
            df = df[df['id'] != id]
            df.to_csv(self.arquivo_csv, index=False)
            registrar_log(f"PACIENTE EXCLUÍDO: ID={id}")
            return True
        return False
