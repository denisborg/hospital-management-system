class Procedimento:
    def __init__(self):
        self.procedimentos = []

    def cadastrar(self):
        nome = input('Nome do procedimento: ')
        preco = input('Preço do procedimento: ')
        self.procedimentos.append({'nome': nome, 'preco': preco})
        print('Procedimento cadastrado com sucesso!')

    def listar(self):
        if not self.procedimentos:
            print('Nenhum procedimento cadastrado.')
        else:
            print('\nLista de Procedimentos:')
            for i, p in enumerate(self.procedimentos):
                print(f"{i+1} - Nome: {p['nome']}, Preço: R$ {p['preco']}")

    def excluir(self):
        self.listar()
        index = int(input('Digite o número do procedimento que deseja excluir: ')) - 1
        if 0 <= index < len(self.procedimentos):
            removido = self.procedimentos.pop(index)
            print(f"Procedimento {removido['nome']} removido com sucesso.")
        else:
            print('Índice inválido.')