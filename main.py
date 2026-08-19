from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome=None, sal_bruto=0, sal_min=1621, inss=7.5):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.sal_min = sal_min
        self.inss = inss

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        pass