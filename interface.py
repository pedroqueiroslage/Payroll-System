from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
from rich.table import Table


class Funcionario(ABC):
    def __init__(self, nome=None, sal_min=1621):
        self.nome = nome
        self.sal_min = sal_min
        self.sal_bruto = 0.0
        self.desc_inss = 0.0
        self.sal_liq = 0.0
        try:
            with open('Funcionarios.txt', 'a', encoding='utf-8'):
                pass
        except Exception as e:
            print(f'ERRO {e}')

    def calc_inss(self):
        if self.sal_bruto <= 1412:
            aliquota = 0.075
        elif 1412.01 <= self.sal_bruto <= 2666.68:
            aliquota = 0.09
        elif 2666.69 <= self.sal_bruto <= 4000.03:
            aliquota = 0.12
        else:
            aliquota = 0.14
        self.desc_inss = self.sal_bruto * aliquota
        return self.desc_inss

    @abstractmethod
    def calc_sal(self):
        pass

    @classmethod
    def analisar_sal(cls):
        try:
            with open('Funcionarios.txt', 'r', encoding='utf-8') as arq:
                linhas = arq.readlines()
                for c in linhas:
                    if not c.strip():
                        continue
                    dados = c.strip().split(' | ')
                    spm = float(dados[1]) / 1621
                    conteudo = (
                        f'O salário de {dados[0]} é de R${float(dados[1]):.2f} e corresponde á {spm:.2f} salários'
                        f' mínimos!').replace('.', ',')
                    print(Panel(conteudo, width=40))
        except Exception as e:
            print(f'ERRO {e}')

    def cad_funcionario(self):
        try:
            self.calc_sal()
            with open('Funcionarios.txt', 'a', encoding='utf-8') as arq:
                arq.write(f'{self.nome} | {self.sal_liq:.2f} | {self.__class__.__name__} | {self.sal_bruto:.2f} '
                          f'| {self.desc_inss:.2f}\n')
        except Exception as e:
            print(f'ERRO {e}')

    def rem_funcionario(self):
        try:
            cont = 0
            novas_linhas = []
            with open('Funcionarios.txt', 'r', encoding='utf-8') as arq:
                linhas = arq.readlines()
                for c in linhas:
                    if not c.strip():
                        continue
                    dados = c.strip().split(' | ')
                    nome = dados[0]
                    cargo = dados[2]
                    if nome.lower() == self.nome.lower() and cargo == self.__class__.__name__:
                        pass
                    else:
                        novas_linhas.append(c)
                        cont += 1
                    if cont == len(linhas):
                        print('[red]Não há nenhum funcionário registrado com este nome no sistema![/]')
            with open('Funcionarios.txt', 'w', encoding='utf-8') as arq:
                print('[blue]Funcionário removido com sucesso![/]')
                for linhas in novas_linhas:
                    arq.write(linhas)
        except Exception as e:
            print(f'ERRO {e}')

    @classmethod
    def relatorio(cls):
        try:
            table = Table(title='Relatório Geral de Funcionarios')
            table.add_column('Nome', style='cyan')
            table.add_column('Salário', style='green')
            table.add_column('Tipo', style='magenta')
            table.add_column('Salário Bruto', style='yellow')
            table.add_column('Desconto INSS', style='red')
            with open('Funcionarios.txt', 'r', encoding='utf-8') as arq:
                linhas = arq.readlines()
                for c in linhas:
                    if not c.strip():
                        continue
                    dados = c.strip().split(' | ')
                    table.add_row(dados[0], f'R${dados[1]}', dados[2], dados[3], dados[4])
            print(table)
        except FileNotFoundError:
            print('Não há funcionários registrados!')
        except Exception as e:
            print(f'ERRO {e}')

    @classmethod
    def res_empresa(cls):
        soma_bruto = 0
        soma_inss = 0
        try:
            with open('Funcionarios.txt', 'r', encoding='utf-8') as arq:
                linhas = arq.readlines()
                for c in linhas:
                    if not c.strip():
                        continue
                    dados = c.strip().split(' | ')
                    soma_bruto += float(dados[3])
                    soma_inss += float(dados[4])
        except Exception as e:
            print(f'ERRO {e}')
        finally:
            print(f'A soma dos salários brutos é de [green]R${soma_bruto:.2f}[/], enquanto o total equivalente '
                  f'ao INSS é de [green]R${soma_inss:.2f}[/]!')