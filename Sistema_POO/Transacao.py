from Cadastro import Cadastro

class Transacao:
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def saque(self):
        self.extrato

        sacar = float(input('SAQUE DE: R$'))
        if sacar > self.saldo : print('Você não possui saldo o suficiente!')
        elif sacar > 1500 : print('Para saques acima de 1500 é necessário a ida até a agência')
        else:
            self.saldo -= sacar
            self.extrato.append(f'SAQUE: R${sacar:.2f}')
            return f'Foi realizado um saque de R${sacar:.2f}'

    def deposito(self):
        self.extrato

        deposite = float(input('DEPOSITAR: R$'))
        self.saldo += deposite
        self.extrato.append(f'DEPÓSITO: R${deposite:.2f}')
        return f'Um valor de: R${deposite} foi depositado em sua conta.'
    
    def transferir(self, quem_recebe):
        quem_recebe
        transferencia = float(input(f'Quanto quer transferir: R$'))
        if transferencia > self.saldo: print('Você não possui saldo o suficiente!')
        else:
            self.saldo -= transferencia
            self.extrato.append(f'TRANSFERÊNCIA REALIZADA: R${transferencia:.2f}')

            quem_recebe.saldo += transferencia
            quem_recebe.extrato.append(f'TRANSFERÊNCIA RECEBIDA: R${transferencia:.2f}')


    def ver_extrato(self):
        return(f'''EXTRATO: {self.extrato} \n
                SALDO RESTANTE: R$ {self.saldo}''')
    
Rune = Transacao()
Emilly = Transacao()

Rune.deposito()
Emilly.deposito()
Emilly.saque()
Rune.transferir(Emilly)
print(Emilly.ver_extrato())