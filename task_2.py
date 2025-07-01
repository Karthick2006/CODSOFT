def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Error: Cannot divide by zero"
    return x / y

def main():
    print("==== Simple Calculator ====")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("⚠️ Please enter valid numbers.")
        return

    print("\nChoose an operation:")
    print(" +  : Addition")
    print(" -  : Subtraction")
    print(" *  : Multiplication")
    print(" /  : Division")

    operation = input("Enter your choice (+, -, *, /): ")

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        print("⚠️ Invalid operation selected.")
        return

    print(f"\n✅ Result: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
