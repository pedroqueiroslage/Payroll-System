from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome=None, sal_bruto=0, sal_min=1621, inss=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.sal_min = sal_min
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