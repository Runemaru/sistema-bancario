#Sistema bancário feito utilizando apenas de dados do tipo [List], estruturas de repetição e condicionais.

LIMITE_DE_SAQUES = 0
SALDO = 0
valor_deposito = []
valor_saque = []

while True:
    print(25 * '-', 25 * '-')
    sistema = int(input(
    '''
    Digite conforme sua necessidade:

    (1) Sacar
    (2) Depositar
    (3) Visualizar Extrato
    (0) Encerrar Sistema
    Digite o número de acordo com sua necessidade:'''))

    if sistema == 1:
        while LIMITE_DE_SAQUES < 3:

            print(25 * '-', 25 * '-')

            saque = float(input('Digite valor que gostaria de sacar:'))
            valor_saque.append(f'R${saque:.2f}')
            LIMITE_DE_SAQUES += 1

            if saque > SALDO:
                print(25 * '-', 25 * '-')
                print('Você não possui o valor solicitado para saque.')
                LIMITE_DE_SAQUES -= 1

                continuando = int(input('Digite [1] para retornar ao menu principal:'))
                print(25 * '-', 25 * '-')

                if continuando == 1:
                    break
                
            elif saque > 500:
                print(25 * '-', 25 * '-')

                print('O valor para saque deve ser igual ou inferior a R$500,00')
                LIMITE_DE_SAQUES -= 1

                print(25 * '-', 25 * '-')

            elif LIMITE_DE_SAQUES == 3:
                print(25 * '-', 25 * '-')

                print('Você atingiu o limite de saques diários.')

                print(25 * '-', 25 * '-')   
                
            else:
                print(25 * '-', 25 * '-')

                print(f'O valor de R${saque:.2f} foi removido de sua conta com sucesso.')
                SALDO -= saque

                print(25 * '-', 25 * '-')
    
    elif sistema == 2:
        print(25 * '-', 25 * '-')

        depositar = float(input('Quanto gostaria de depositar:'))
        valor_deposito.append(f'R${depositar:.2f}')

        print(f'O valor de R${depositar:.2f} foi depositado em sua conta corrente.')
        SALDO += depositar

        print(25 * '-', 25 * '-')
    
    elif sistema == 3:

        print(25 * '-', 'EXTRATO', 25 * '-')

        extrato = int(input('Gostaria de visualizar o extrato (Sim [1] ]Não [2]):'))
        if extrato == 1:
                
                print(f'DEPOSITOS:\n{valor_deposito}')
                print(f'SAQUES:\n {valor_saque}')
                print('SALDO RESTANTE:\n' f'R$ {SALDO:.2f}')
                 

        print(25 * '-', 'EXTRATO', 25 * '-')
    
    else:
        print('Obrigado por utilizar nossos serviços!')
        break