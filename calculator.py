from time import sleep as sl


while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'power' to raise a number to the power of another number")
    print("Enter 'modulo' to calculate the modulo of two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    if user_input == "quit":
        break

    elif user_input == "add":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            print(f"The answer is {num1 + num2}")
            print(".")
            print(".")
        except OverflowError:
            print("Error, result is too large!")
        finally:
            sl(2)

    elif user_input == "subtract":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            print(f"The answer is {num1 - num2}")
            print(".")
            print(".")

        except OverflowError:
            print("Error, result is too large!")
        finally:
            sl(2)

    elif user_input == "multiply":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            print(f"The answer is {num1 * num2}")
            print(".")
            print(".")
        except OverflowError:
            print("Error, result is too large!")
        finally:
            sl(2)

    elif user_input == "divide":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            print(f"The answer is {num1 / num2}")
            print(".")
            print(".")
        except OverflowError:
            print("")
            print("Error, result is too large!")
        finally:
            sl(2)

    elif user_input == "power":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            print(f"The answer is {str(num1 ** num2)}")
            print(".")
            print(".")
        except OverflowError:
            print("Error, result is too large!")
        finally:
            sl(2)

    elif user_input == "modulo":
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            print(f"The answer is {str(num1 % num2)}")
            print(".")
            print(".")
        except OverflowError:
            print("Error, result is too large!")
        finally:
            sl(2)
    else:
        print("Unknown input")
        sl(2)
