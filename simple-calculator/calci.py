while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        operation = input("Enter the operation you want to perform:\n+ for Addition\n- for Subtraction\n* for Multiplication\n/ for Division: ")
        match operation:
            case "+":
                print(f"The sum of {a} and {b} is {a+b}")
            case "-":
                print(f"The difference of {a} and {b} is {a-b}")
            case "*":
                print(f"The product of {a} and {b} is {a*b}")
            case "/":
                if b == 0:
                    print("You cannot divide by zero")
                else:
                    print(f"The division of {a} and {b} is {a/b}")
            case _:
                print("Enter the correct operation you want to perform")
    except ValueError:
        print("Invalid input. Enter correct input")
        continue
    answer = input("Enter any other key to continue. 'q' for quit: ").lower()
    if answer == "q":
            print("Exiting calculator..")
            break