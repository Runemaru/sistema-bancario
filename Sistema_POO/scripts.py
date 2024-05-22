def inicio_sistema():
    return '''
    Possui cadastro em nosso sistema bancário?
    { Caso resposta positiva: Digite [1] }
    { Caso resposta negativa: Digite [2] }
    Digite:'''


def acessar_cadastro():
    return '''

    {Para acessar nosso sistema bancário}
{É necessário que tenha as seguintes informações:}

            { Nome completo }
                { Idade }
                 { CPF }

    {Para realizar o cadastro:  Digite [ 1 ]}
    {Para encerrar a aplicação: Digite [ 2 ]}
    Digite:'''



def acessar_transacoes():
    return '''

Digite o número de acordo com sua necessidade:

[ 1 ] - Realizar depósito.
[ 2 ] - Realizar saque.
[ 3 ] - Realizar transferência.
[ 4 ] - Solicitar extrato.
[ 5 ] - Encerrar o sistema.
Digite:'''

def continuar_cadastro():
    return'''

Gostaria de cadastrar outro usuário?
[1] Para sim
[2] Para não
Digite sua resposta:'''