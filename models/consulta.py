import pandas as pd
import os
from datetime import datetime

class Consulta:
    def __init__(self):
        self.arquivo = 'dados/consulta.csv'
        self.arquivo_id = 'dados/ultimo_id_consulta.txt'
        os.makedirs('dados', exist_ok=True)

        if not os.path.exists(self.arquivo) or os.path.getsize(self.arquivo) == 0:
            df = pd.DataFrame(columns=['id', 'paciente', 'data', 'medico'])
            df.to_csv(self.arquivo, index=False)

        if not os.path.exists(self.arquivo_id):
            with open(self.arquivo_id, 'w') as f:
                f.write('0')

    def validar_data(self, data_str):
        try:
            datetime.strptime(data_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def gerar_novo_id(self):
        with open(self.arquivo_id, 'r') as f:
            ultimo_id = int(f.read())
        novo_id = ultimo_id + 1
        with open(self.arquivo_id, 'w') as f:
            f.write(str(novo_id))
        return novo_id

    def cadastrar(self):
        paciente = input('Nome do paciente: ')
        
        data = input('Data da consulta (dd/mm/aaaa): ')
        while not self.validar_data(data):
            print("Formato inválido. Tente novamente.")
            data = input('Data da consulta (dd/mm/aaaa): ')
        
        medico = input('Nome do médico: ')
        novo_id = self.gerar_novo_id()

        nova_linha = pd.DataFrame([{
            'id': novo_id,
            'paciente': paciente,
            'data': data,
            'medico': medico
        }])

        df = pd.read_csv(self.arquivo)
        df = pd.concat([df, nova_linha], ignore_index=True)
        df.to_csv(self.arquivo, index=False)
        print(f'Consulta cadastrada com sucesso! ID: {novo_id}')

    def listar(self):
        df = pd.read_csv(self.arquivo)
        if df.empty:
            print('Nenhuma consulta cadastrada.')
        else:
            df = df.sort_values(by='id')
            print(df[['id', 'paciente', 'data', 'medico']].to_string(index=False))

    def editar(self):
        df = pd.read_csv(self.arquivo)
        if df.empty:
            print("Nenhuma consulta para editar.")
            return

        print(df.to_string(index=False))
        try:
            id_editar = int(input("Digite o ID da consulta que deseja editar: "))
        except ValueError:
            print("ID inválido.")
            return

        if id_editar not in df['id'].values:
            print("ID não encontrado.")
            return

        linha = df[df['id'] == id_editar].iloc[0]

        novo_paciente = input(f"Novo nome do paciente (Enter para manter '{linha['paciente']}'): ") or linha['paciente']
        nova_data = input(f"Nova data (Enter para manter '{linha['data']}'): ") or linha['data']
        while not self.validar_data(nova_data):
            print("Formato de data inválido. Tente novamente.")
            nova_data = input(f"Nova data (Enter para manter '{linha['data']}'): ") or linha['data']

        novo_medico = input(f"Novo nome do médico (Enter para manter '{linha['medico']}'): ") or linha['medico']

        df.loc[df['id'] == id_editar, ['paciente', 'data', 'medico']] = [novo_paciente, nova_data, novo_medico]
        df.to_csv(self.arquivo, index=False)
        print("Consulta atualizada com sucesso.")

    def excluir(self):
        df = pd.read_csv(self.arquivo)
        if df.empty:
            print("Nenhuma consulta para excluir.")
            return

        print(df.to_string(index=False))
        try:
            id_excluir = int(input("Digite o ID da consulta que deseja excluir: "))
        except ValueError:
            print("ID inválido.")
            return

        if id_excluir not in df['id'].values:
            print("ID não encontrado.")
            return

        confirm = input(f"Tem certeza que deseja excluir a consulta com ID {id_excluir}? (s/n): ").strip().lower()
        if confirm != 's':
            print("Exclusão cancelada.")
            return

        df = df[df['id'] != id_excluir]
        df.to_csv(self.arquivo, index=False)
        print(f"Consulta com ID {id_excluir} excluída com sucesso.")
