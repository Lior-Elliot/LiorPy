nome = ''
dindin = 0
while True:
    valor = input('> ')
    if valor == 'help':
        print('''
            1 - Cadastro
            2 - Dados Cliente
            3 - Depositar
            4 - Pagar
            5 - Sair
            ''')
    if valor == '1':
        nome = input('Qual é seu nome? ')

    if valor == '2':
        if nome == '':
            print('Você não tem nome')
        else:
            print('seu nome é ' +nome)
        print('Você tem '+ str(dindin) +' dindins')

    if valor == '3':
        deposito = int(input('Quanto você quer depositar? $'))
        dindin = dindin + deposito
    
    if valor == '4':
        Pago = int(input('Quanto você quer pagar? $'))
        dindin = dindin - Pago
        input('Para quem você quer pagar? ')
        print('Não interessa')
    
    if valor == '5':
        break
    
