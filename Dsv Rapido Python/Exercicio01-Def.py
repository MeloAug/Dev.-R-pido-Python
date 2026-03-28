#Funções em Python são blocos de códigos reutilizáveis que executam tarefas especificas
#organizando o programa e evitando repetição
#Definidas com a palavra-chave def, podem receber parâmetros (entradas)
# e retornar resultados (saidas) com return
#tornam o código mais legível, estruturado e eficiente
def saudacao(nome):                     #def nome(parâmetro)
    return f"Olá, {nome}!"              #retorno
mensagem = saudacao("Maria")            #Chamada da função
print(mensagem)
#outro exemplo
def dizer_ola():
    print("Olá, mundo!")
dizer_ola()