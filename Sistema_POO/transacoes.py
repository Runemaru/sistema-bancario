from cadastro import Cadastro

class Transacoes(Cadastro):
    saldo : float = 0 #Nesta linha determinamos que o objeto ''saldo'' recebe elementos do tipo float.
                      #E que receberá um valor inicial, que será 0.
    
    def deposito(self, dinheiro : float):
        self.dinheiro = dinheiro
        self.saldo += dinheiro

x = Transacoes('Rune', 18, '12345678910', 0)
print(x.primeiro_acesso())
print(x.validar_CPF())

x.deposito(2500)
print(x)
