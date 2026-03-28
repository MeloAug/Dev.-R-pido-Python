#Exemplo de programa Python com função para calcular a média
def calcular_media(nota1, nota2, nota3):
    """Calcula a média de tres e retornar o resultado"""
    media = (nota1 + nota2 + nota3) / 3
    return media
#--- Corpo principal do programa ---
#1. entrada de dados
n1 = float (input("digite a nota 1: "))
n2 = float (input("Digite a nota 2: "))
n3 = float (input("Digite a nota 3:"))

#2. Chamada da função
resultado_media = calcular_media(n1, n2, n3)

#3. Saida do resultado
print(f"Amédia dinal é: {resultado_media:.1f}")

if resultado_media >=7:
    print("Aprovado")
else:
    print("Reprovado")