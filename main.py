from menu import *
from employees_type import *


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
                    print('[yellow]Funcionário Registrado![/]')
                    p1 = Horista(f'{func}', vlrh, hrt)
                    p1.cad_funcionario()
                elif p == 'M':
                    func = str(input('Seu nome: '))
                    slr = int(input('Salário bruto: R$'))
                    print('[yellow]Funcionário Registrado![/]')
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
        elif p1 == '3':
            Funcionario.relatorio()
        elif p1 == '4':
            Funcionario.res_empresa()
        elif p1 == '5':
            Funcionario.analisar_sal()
        elif p1 == '0':
            print('[blue]Fechando Sistema...[/]')
            break
        else:
            print('[red]Resposta Inválida![/]')


if __name__ == '__main__':
    main()