import operator

def calculator_menu():
    print(calculator_menu)
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Modulus")
    print("6.Check greater number")


def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choices (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choices. Enter the number of 1-6 ")
        except ValueError:
            print("Invalid input choices. Please enter a valid number.")

def get_user_inputs():
    try:
        ColumnA = float(input("Enter first number: "))
        ColumnB= float(input("Enter second number: "))
        return ColumnA, ColumnB
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None, None

def perform_operation(choice, num1, num2):
    operations = {
        1: operator.add,
        2: operator.sub,
        3: operator.mul,
        4: operator.truediv,
        5: operator.mod,
        6: max  # Check greater number
    }

    operation_function = operations[choice]
    result = operation_function(num1, num2)
    return result

if __name__ == "__main__":
    calculator_menu()
    choice = get_user_choice()

    num1, num2 = get_user_inputs()
    if num1 is not None and num2 is not None:
        result = perform_operation(choice, num1, num2)
        print(f"Result: {result}")