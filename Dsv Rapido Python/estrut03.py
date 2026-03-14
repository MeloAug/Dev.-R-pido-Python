usuario = ''
senha = ''
tentativas = 0
while(usuario!='Aug' and senha!='123') and tentativas <3:
    usuario= input('Digite seu usuario: ')
    senha= input('Digite sua senha: ')
    tentativas= tentativas + 1
    print ('Tente novamente')
if usuario!='Aug' and senha!='123':
    print('Aguarde 30min e tente novamente')
else:
    print('Login feito com sucesso')