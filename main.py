from abc import ABC, abstractmethod
from rich import print
#   from rich.panel import Panel


class Funcionario(ABC):
    def __init__(self, nome=None, sal_bruto=0, sal_min=1621, inss=0.0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.sal_min = sal_min
        if sal_bruto <= 1412:
            self.inss = 0.075
        elif 1412.01 < sal_bruto < 2666.68:
            self.inss = 0.09
        elif 2666.69 < sal_bruto < 4000.03:
            self.inss = 0.12
        elif 4000.03 < sal_bruto:
            self.inss = 0.14
        else:
            self.inss = inss

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
        self.inss = self.sal_bruto * self.inss
        salf = self.sal_bruto - self.inss
        print(salf)


class Mensalista(Funcionario):
    def calc_sal(self):
        pass


def main():
    # p = str(input('Qual tipo de funcionario?\nH = Horista\nM = Mensalista\n'))
    # if p == 'H':
    #     Horista('Pedro', 50, 30)
    Horista('Pedro', 50, 30)


if __name__ == '__main__':
    main()