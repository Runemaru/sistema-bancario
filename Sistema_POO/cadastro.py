#Sistema bancário feito utilizando programação orientada a objeto, aqui nós iremos tentar aproveitar o máximo possível do assunto
#Colocando em prática as ideias de polimorfismo, herança, abstração, construtores, getters, setters, properties, e as demais práticas do POO.

### IMPORTS ###

from dataclasses import dataclass #Este é um modulo padrão que visa facilitar o processo de utilização da POO, encurtando as declarações.
from random import randint
#############################

@dataclass #Esta propriedade é um decorador que fará com que o módulo dataclasses funcione.
# É necessário chamá-lo sempre que você quer criar uma nova classe, caso esteja utilizando o módulo.
class Cadastro:
    nome : str
    idade : int
    CPF : str
    AGENCIA : int = 0 #Podemos declarar a variavel como tipo None e fazê-lá assumir um tipo diferente de dado por uma função
                      #Assim como podemos assumir que ela receberá determinado tipo de dado, e que seu valor será 0, ou vazio
                      #E assim fazê-la assumir um determinado valor por uma função.
                      #Por algum motivo mesmo tentando utilizar AGENCIA = 0, a mesma não assumiu o valor da função primeiro_acesso.
                      #Assumindo apenas após ser declarado que receberia um atributo inteiro = 0. Como está escrito em código.


    def primeiro_acesso(self):
        self.AGENCIA = randint(1000,1100)
        return f'Seja bem-vindo {self.nome}, você foi designado para a agência de número {self.AGENCIA}.'
    
    def validar_CPF(self):
            if len(self.CPF) != 11:
                print('Quantia de números divergente do necessário. Favor recadastrar.')

            if not self.CPF.isdigit(): #Aqui estamos utilizando uma função de string. Que vê se uma string esta recebendo números.
                return f'Caractéres invalidos para CPF. Favor recadastrar.' #Para que caso receba algo diferente de números imprima isto.
            else:
                 return f'CPF válido.' #E que caso isdigit seja verdadeiro, você retorne este valor. Mostrando que há apenas números.