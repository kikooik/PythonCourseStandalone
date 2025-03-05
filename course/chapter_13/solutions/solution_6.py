def create_operation(op):
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    if op == "add":
        return add
    elif op == "subtract":
        return subtract
    elif op == "multiply":
        return multiply
    elif op == "divide":
        return divide