operator = input("Enter an operator (+ - * /): ").strip()
quantity = input("Enter quantity of numbers (2 or 3): ").strip()

if quantity not in ("2", "3"):
    print("Invalid quantity. Please enter 2 or 3.")
else:
    try:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        
        if quantity == "3":
            num3 = float(input("Enter 3rd number: "))

        if operator == "+":
            result = num1 + num2 + (num3 if quantity == "3" else 0)
        elif operator == "-":
            result = num1 - num2 - (num3 if quantity == "3" else 0)
        elif operator == "*":
            result = num1 * num2 * (num3 if quantity == "3" else 1)
        elif operator == "/":
            if num2 == 0 or (quantity == "3" and num3 == 0):
                print("Error: Division by zero is not allowed.")
                result = None
            else:
                result = num1 / num2 / (num3 if quantity == "3" else 1)
        else:
            print(f"'{operator}' is not a valid operator.")
            result = None

        if result is not None:
            print(round(result, 3))

    except ValueError:
        print("Invalid input! Please enter valid numbers.")