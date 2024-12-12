def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calcDictionary = {"+": add, "-": subtract, "*":multiply, "/": divide}
cont = "n"
# f_num = 0
while True:
    if cont == "n":
        f_num = float(input("what's the first number? "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    s_num = float(input("What's the next number?"))
    result = calcDictionary[operation](f_num, s_num)
    print(f"{f_num}{operation}{s_num} = {result}")
    cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start calculation:")
    if cont == "y":
        f_num = result