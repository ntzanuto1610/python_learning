tamanho = int(input("digite o tamanho da sequencia de numeros: "))

produto = 1
i = 0

while  i < tamanho:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i += 1
print("A produto dos valores digitados eh: ", produto)
