num1 = float(input("Ensira o primeiro número: "))
op = input("Ensira o operador: ")
num2 = float(input("Ensira o segundo número: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Operador inválido!")