from abc import ABC, abstractmethod
from rich import print
#   from rich.panel import Panel


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
        pass

    def cad_funcionario(self):
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
    def calc_sal(self):
        pass


def main():
    p = str(input('Qual tipo de funcionario?\nH = Horista\nM = Mensalista\n'))
    if p == 'H':
        p1 = Horista('Pedro', 50, 100)
        p1.calc_sal()


if __name__ == '__main__':
    main()