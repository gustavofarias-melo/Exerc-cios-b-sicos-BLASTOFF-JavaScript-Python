num = int(input("Digite um número para checar: "))

if num > 1:

    for i in range(2, num):

        if (num % i) == 0:
            print(num, " NÃO é um número primo")
            break
    else:
        print(num, " é um número primo.")

else:
    print("Digite um valor maior que 1")
