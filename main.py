class Initialize(): 

    def show_menu(self): 
        print('\n')
        print(50 * '-')
        print('Bem-vindo ao Sistema do Hospital!')
        print(50 * '-')

        print('1 - Pacientes')
        print('2 - Consultas')
        print('3 - Procedimentos')
        print('4 - Sair') 

    def choose_option(self):
        option = input('\nEscolha uma das opções: ')

        if option != '1' and option != '2' and option != '3' and option != '4':
            print('\nOpção inválida!')

        return option

    def show_sub_menu(self, option):
        print('\n')
        print(50 * '-')
        if (option == '1'):  
            print('Pacientes:')
        elif (option == '2'):
            print('Consultas:')
        elif (option == '3'):
            print('Procedimentos:')
        print(50 * '-')

        print('1 - Cadatrar')
        print('2 - Listar')
        print('3 - Excluir')
        print('4 - Voltar') 

    def choose_sub_option(self):
        sub_option = input('\nEscolha uma das opções: ')

        if sub_option != '1' and sub_option != '2' and sub_option != '3' and sub_option != '4':
            print('\nOpção inválida!')

        return sub_option

    def to_go_out(self):
        print('\nObrigado, volte sempre!')

if __name__ == "__main__":
    init = Initialize()
    option = ''

    while option != '4':
        init.show_menu()
        option = init.choose_option()

        if option in ('1','2','3'):
            sub_option = ''

            while sub_option != '4':
                init.show_sub_menu(option)
                sub_option = init.choose_sub_option()

                if sub_option == '1': ### Pacientes
                    pass

                elif sub_option == '2': ### Consultas
                    pass

                elif sub_option == '3': ### Procedimentos
                    pass

        elif option == '4':
            init.to_go_out()
