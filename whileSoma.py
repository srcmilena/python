print("Digite uma sequência de valores e digite zero quando quiser fazer a soma. ")
soma = 0

valor = 1
while valor != 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor

print("A soma dos valores digitados é: ", soma)