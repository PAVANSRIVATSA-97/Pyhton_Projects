questions = [
    ["Q1. Which module is best for CPU-bound tasks in Python?", "threading", "multiprocessing", "math", "sys", 2],
    ["Q2. What does 'while q:' evaluate to if q is an empty list []?", "True", "False", "None", "Error", 2],
    ["Q3. How does Python handle traditional Method Overloading?", "By checking argument types", "By checking argument count", "It doesn't; the last definition wins", "By using the 'overload' keyword", 3],
    ["Q4. Which 'sys' attribute is a list containing command-line arguments?", "sys.path", "sys.version", "sys.exit", "sys.argv", 4],
    ["Q5. What is the correct 'default' case symbol in a Python match-case block?", "default:", "else:", "*:", "_:", 4],
    ["Q6. Which method is called when you use the + operator on a custom object?", "__sum__", "__add__", "__plus__", "__math__", 2],
    ["Q7. Which Git button in VS Code automates staging and committing?", "Yes", "Always", "Never", "Cancel", 2],
    ["Q8. What is the purpose of the 'finally' block in exception handling?", "To run only if an error occurs", "To run only if no error occurs", "To run regardless of whether an error occurred", "To skip the error message", 3]
]

prize_money = [100,200,300,400,500,600,700,800]
i = 0
sum = 0
for question in questions:
    print(question[0])
    print(f"Option 1: {question[1]}")
    print(f"Option 2: {question[2]}")
    print(f"Option 3: {question[3]}")
    print(f"Option 4: {question[4]}")

    print("Enetr 1 for Option 1, 2 for Option 2, 3 for Option 3, 4 for Option 4")
    inp = int(input("Enter your answer: "))
    
    if (inp == question[5]):
        sum += prize_money[i]
        print("Correct answer")
        print(f"You have won {sum}")
        i += 1
        if (question[0] == "Q4. Which 'sys' attribute is a list containing command-line arguments?"):
            print("You have reached checkpoint")
    else:
        print("Sorry! You loose")
        print(f"Correct option was {question[5]}")
        print(f"You take home {sum}")
        break
print("The game has ended")