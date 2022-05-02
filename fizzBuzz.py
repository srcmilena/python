numero = int(input("Digite um número de 0 a 10: "))
numero2 = int(input("Digite um outro número de 0 a 10: "))

if (numero % 3) == 0 and (numero2 % 5) == 0:
    print("FizzBuzz")

else: 
    print(numero, numero2)