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
        pass

    def rem_funcionario(self):
        pass

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
        print(self.sal_liq)


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.calc_inss()
        self.sal_liq = self.sal_bruto - self.desc_inss
        print(self.sal_liq)


def main():
    while True:
        try:
            p = str(input('Qual tipo de funcionario?\nH = Horista\nM = Mensalista\n').strip()[0]).upper()
            if p == 'H':
                p1 = Horista('Pedro', 50, 100)
                p1.calc_sal()
            elif p == 'M':
                p1 = Mensalista('Pedro', 6000)
                p1.calc_sal()
                p1.analisar_sal()
            else:
                print('[red]Resposta Inválida![/]')
        except Exception as e:
            print(f'ERRO {e}')
            break


if __name__ == '__main__':
    main()