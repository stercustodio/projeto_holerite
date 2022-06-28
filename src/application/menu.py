

class Menu():

    @staticmethod
    def menu(titulo, opcoes):
        while True:
            print("=" * len(titulo), titulo, "=" * len(titulo), sep="\n")
            for i, (opcao, funcao) in enumerate(opcoes, 1):
                print("[{}] - {}".format(i, opcao))
            print("[{}] - Retornar/Sair".format(i+1))
            op = input("Opção: ")
            if op.isdigit():
                if int(op) == i + 1:
                    # Encerra este menu e retorna a função anterior
                    break
                if int(op) <= len(opcoes):
                    # Chama a função do menu:
                    opcoes[int(op) - 1][1]()
                    continue
            print("Opção inválida. \n\n")

    @staticmethod
    def principal():
        opcoes = [
            ("Cadastro de funcionarios", Menu.funcionarios),
            ("Cadastro de cargo", Menu.cargo),
            ("Holerite", Menu.holerite),
        ]
        return Menu.menu("# MENU PRICIPAL #", opcoes)

    @staticmethod
    def funcionario():
        opcoes = [
            ("Inserir funcionario", Menu.selecionar_opcoes),
            ("Consultar funcionario", Menu.selecionar_opcoes),
            ("Remover funcionario", Menu.selecionar_opcoes),
            ("Listar todos", Menu.selecionar_opcoes),
        ]
        return Menu.menu("# MENU DE CLIENTES #", opcoes)

    @staticmethod
    def cargo():
        opcoes = [
            ("Inserir cargo", Menu.selecionar_opcoes),
            ("Consultar cargo", Menu.selecionar_opcoes),
            ("Remover cargo", Menu.selecionar_opcoes),
            ("Listar todos", Menu.selecionar_opcoes),
        ]
        return Menu.menu("# MENU DE CARGOS #", opcoes)

    # @staticmethod
    # def holerite():
    #     opcoes = [
    #         ("Registar ", Menu.selecionar_opcoes),
    #         ("Consultar ", Menu.selecionar_opcoes),
    #         ("Listar ", Menu.selecionar_opcoes),
    #         ("Listar ", Menu.selecionar_opcoes),
    #     ]
    #     return Menu.menu("# MENU DE HOLERITE #", opcoes)

    @staticmethod
    def selecionar_opcoes():
        print("teste")
