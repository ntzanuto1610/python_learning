print("Digite uma sequencia de valores terminada por zero: ")
produto = 1

valor = 1
while valor !=0:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor

print("A produto dos valores digitados eh: ", produto)
