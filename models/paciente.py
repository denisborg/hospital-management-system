import os
import pandas as pd
from utils.configs import Configuracoes

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

    def cadastrar(self):
        nome = input('Nome do paciente: ')
        cpf = input('CPF do paciente: ')
        data_nasc = input('Data de Nascimento: ')
        sexo = input('Sexo: ')

        novo_id = self.gerar_novo_id()
        novo_paciente = pd.DataFrame([[novo_id, nome, cpf, data_nasc, sexo]], 
                                    columns=['id', 'nome', 'cpf', 'data_nasc', 'sexo'])
        
        # Adiciona ao arquivo existente
        novo_paciente.to_csv(self.arquivo_csv, mode='a', header=False, index=False)
        print(f'Paciente cadastrado com sucesso! ID: {novo_id}')

    def listar(self):
        df = pd.read_csv(self.arquivo_csv)
        
        if df.empty:
            print('Nenhum paciente cadastrado.')
        else:
            print('\nLista de Pacientes:')
            for index, row in df.iterrows():
                print(f"ID: {row['id']}, Nome: {row['nome']}, CPF: {row['cpf']}, Data de Nascimento: {row['data_nasc']}, Sexo: {row['sexo']}")

    def excluir(self):
        df = pd.read_csv(self.arquivo_csv)
        
        if df.empty:
            print('Nenhum paciente para excluir.')
            return

        self.listar()
        id_excluir = input('Digite o ID do paciente que deseja excluir: ').strip()
        
        # Converter para string para evitar problemas de tipo
        df['id'] = df['id'].astype(str)
        
        tamanho_inicial = len(df)
        df = df[df['id'] != id_excluir]
        
        if len(df) < tamanho_inicial:
            df.to_csv(self.arquivo_csv, index=False)
            print(f'Paciente com ID {id_excluir} removido com sucesso')
        else:
            print('ID não encontrado.')

    def editar(self):
        df = pd.read_csv(self.arquivo_csv)
        
        if df.empty:
            print('Nenhum paciente cadastrado para editar.')
            return
       
        id_editar = input('Digite o ID do paciente que deseja editar: ').strip()
        
        # Converter para string para evitar problemas de tipo
        df['id'] = df['id'].astype(str)
        
        if id_editar not in df['id'].values:
            print('ID não encontrado.')
            return
            
        paciente = df[df['id'] == id_editar].iloc[0]
        print("\nDados atuais do paciente:")
        print(f"1. Nome: {paciente['nome']}")
        print(f"2. CPF: {paciente['cpf']}")
        print(f"3. Data de Nascimento: {paciente['data_nasc']}")
        print(f"4. Sexo: {paciente['sexo']}")
        
        campo = input("\nDigite o número do campo que deseja editar (1-4): ")
        novo_valor = input("Digite o novo valor: ")
        
        if campo == '1':
            df.loc[df['id'] == id_editar, 'nome'] = novo_valor
        elif campo == '2':
            df.loc[df['id'] == id_editar, 'cpf'] = novo_valor
        elif campo == '3':
            df.loc[df['id'] == id_editar, 'data_nasc'] = novo_valor
        elif campo == '4':
            df.loc[df['id'] == id_editar, 'sexo'] = novo_valor
        else:
            print("Opção inválida.")
            return
            
        df.to_csv(self.arquivo_csv, index=False)
        print("Paciente atualizado com sucesso!")

    def buscar(self, cpf):
        df = pd.read_csv(self.arquivo_csv)
        
        if df.empty:
            print('Nenhum paciente cadastrado para consultas.')
            return 0

        df['cpf'] = df['cpf'].astype(str)

        if cpf not in df['cpf'].values:
            print('Paciente não encontrado.')
            return 0
            
        paciente = df[df['cpf'] == cpf].iloc[0]
        return paciente['id']
