import cadastro, transacao, execucao, scripts

contador = True
usuarios = []

while contador == True:
    inicio_sistema = int(input(scripts.inicio_sistema()))
    if inicio_sistema == 2:
        print('Estaremos lhe passando para o sistema de cadastro!')
        inicio_cadastro = int(input(scripts.acessar_cadastro()))
        if inicio_cadastro == 2 or inicio_cadastro != 1 and 2:
            print('Sistema encerrado')
            contador = False
        else:
            
            while True:
                x = cadastro.Cadastro
                x.registro_bancario(x)
                x.validar_CPF(x)
                if x.validar_CPF(x) == False:
                    break

                print(f'Seus dados foram registrados em nosso sistema: \n Nome: {x.nome} \n Idade: {x.idade} \n CPF: {x.CPF} \n AGENCIA: {x.AGENCIA}')
                usuarios.append({ 'Nome': x.nome,
                                'CPF': x.CPF,
                                'Idade': x.idade,
                                'AGENCIA': x.AGENCIA})
                
                continuar = int(input(scripts.continuar_cadastro()))
                if continuar == 1:
                    continue
                else:
                    contador = False
                    break
                    
    else:
        contador = False
        verificar_cadastro = input('Digite seu CPF:')
        for usuario in usuarios:
            usuario['CPF']
            if usuario['CPF'] == verificar_cadastro:
                print('CPF presente em sistema.')
            else:
                print('CPF inválido')
                break

for usuario in usuarios:
        print(f'Nome:{usuario['Nome']}, Idade:{usuario['Idade']}, CPF:{usuario['CPF']}, AGÊNCIA:{usuario['AGENCIA']}')