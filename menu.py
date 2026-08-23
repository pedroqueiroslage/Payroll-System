from rich.panel import Panel
from rich import print


class Menu:
    def __init__(self):
        conteudo = ('[blue]Welcome to the Payroll System![/]\nO que deseja fazer?\n'
                    '1 = Registrar novos funcionários\n2 = Remover funcionário\n'
                    '3 = Ver relatório da empresa\n4 = Ver resumo da folha salárial\n'
                    '5 = Analisar Salário\n0 = Fechar sistema')
        print(Panel(conteudo, width=45, title='Payroll System'))