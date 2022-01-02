a = int(input("Valor de a: "));
b = int(input("Valor de b: "));
c = int(input("Valor de c: "));

if (a < b and a < c):
    print(f"{a} é menor.")
elif (b < c):
    print(f"{b} é menor.")
else:
    print(f"{c} é menor.")