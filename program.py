print("Simple Calculator")
print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input("Enter your choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operations = {
    "1": num1 + num2,
    "2": num1 - num2,
    "3": num1 * num2,
    "4": num1 / num2 if num2 != 0 else "Error! Division by zero."
}
result = operations.get(choice, "Invalid choice!")
print("Result:", result)

