atrasos = int(input('Quantas faltas ou atrasos você tem? '))
if atrasos>= 3:
    print("Você esté supenso")
elif atrasos==2:
    print("Mais 1 falta você estará suspenso")
elif atrasos==1:
    print("Mais 2 faltas e estará suspenso")
else:
    print("Pode entrar")