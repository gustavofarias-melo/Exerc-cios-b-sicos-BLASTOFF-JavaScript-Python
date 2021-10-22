print("Digite dois numeros para verificar se são multiplos.")
num1 = int(input("Digite o valor: "))
num2 = int(input("Digite outro valor: "))

if (num1 % num2 == 0 or num2 % num1 == 0):
    print(f"{num1} e {num2} são multiplos.")
else:
    print(f"{num1} e {num2} NÃO são multiplos.")
