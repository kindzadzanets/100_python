
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n1 is None or n2 is None:
        return 0
    else:
        return n1 / n2
    

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    n1 = float(input("Set the first number:\n"))
    next = True

    while next:
        operator = input("Set the action: \n")
        n2 = float(input("Set the second number:\n"))
        result = operators[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
        next = input("Would you like to make operation with result? y or n :\n").lower()
        if next == "y":
            n1 = result
        else:
            next = False
            print("\n" * 5)
            calculator()
            
calculator()
        
