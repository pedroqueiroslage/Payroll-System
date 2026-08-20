from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


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

    def analisar_sal(self):
        spm = self.sal_liq / self.sal_min
        conteudo = (f'O salário de {self.nome} é de R${self.sal_liq:.2f} e corresponde á {spm:.2f} salários'
                    f' mínimos!').replace('.', ',')
        print(Panel(conteudo, width=40))

    def cad_funcionario(self):
        try:
            self.calc_sal()
            with open('Funcionarios.txt', 'a', encoding='utf-8') as arq:
                arq.write(f'{self.nome} | R${self.sal_liq:.2f} | {self.__class__.__name__}\n')
        except Exception as e:
            print(f'ERRO {e}')

    def rem_funcionario(self):
        try:
            novas_linhas = []
            with open('Funcionarios.txt', 'r', encoding='utf-8') as arq:
                linhas = arq.readlines()
                for c in linhas:
                    if not c.strip():
                        continue
                    dados = c.strip().split(' | ')
                    nome = dados[0]
                    cargo = dados[-1]
                    if nome.lower() == self.nome and cargo == self.__class__.__name__:
                        pass
                    else:
                        novas_linhas.append(c)
            with open('Funcionarios.txt', 'w', encoding='utf-8') as arq:
                for linhas in novas_linhas:
                    arq.write(linhas)
        except Exception as e:
            print(f'ERRO {e}')

    def relatorio(self):
        pass

    def res_empresa(self):
        pass


class Horista(Funcionario):
    def __init__(self, nome, val_hora=0, hrs_trab=0):
        super().__init__(nome)
        self.val_hora = val_hora
        self.hrs_trab = hrs_trab

    def calc_sal(self):
        self.sal_bruto = self.val_hora * self.hrs_trab
        self.calc_inss()
        self.sal_liq = self.sal_bruto - self.desc_inss


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.calc_inss()
        self.sal_liq = self.sal_bruto - self.desc_inss


class Menu:
    def __init__(self):
        conteudo = ('[blue]Welcome to the Payroll System![/]\nO que deseja fazer?\n'
                    '1 = Registrar novos funcionários\n2 = Remover funcionário\n'
                    '3 = Ver relatório da empresa\n4 = Ver resumo da folha salárial?\n'
                    '0 = Fechar sistema')
        print(Panel(conteudo, width=50, title='Payroll System'))


def main():
    while True:
        Menu()
        p1 = input('>>> ')
        if p1 == '1':
            try:
                p = str(input('Qual tipo de funcionario deseja registrar?\nH = Horista\nM = '
                              'Mensalista\n').strip()[0]).upper()
                if p == 'H':
                    func = str(input('Seu nome: '))
                    vlrh = int(input('Valor da hora trabalhada: R$'))
                    hrt = int(input('Quantas horas trabalhadas: '))
                    p1 = Horista(f'{func}', vlrh, hrt)
                    p1.cad_funcionario()
                elif p == 'M':
                    func = str(input('Seu nome: '))
                    slr = int(input('Salário bruto: R$'))
                    p1 = Mensalista(f'{func}', slr)
                    p1.cad_funcionario()
                else:
                    print('[red]Resposta Inválida![/]')
            except Exception as e:
                print(f'ERRO {e}')
                break
        elif p1 == '2':
            p = str(input('Qual tipo de funcionario deseja remover?\nH = Horista\nM = '
                          'Mensalista\n').strip()[0]).upper()
            if p == 'H':
                func = str(input('Seu nome: '))
                p1 = Horista(f'{func}', 0, 0)
                p1.rem_funcionario()
            elif p == 'M':
                func = str(input('Seu nome: '))
                p1 = Mensalista(f'{func}', 0)
                p1.rem_funcionario()
            else:
                print('[red]Resposta Inválida![/]')
        elif p1 == '0':
            print('[blue]Fechando Sistema...[/]')
            break


if __name__ == '__main__':
    main()