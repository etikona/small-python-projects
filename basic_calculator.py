# Define the functions needed for, add, sub, mul, div
# Print options to the user
# Ask for values
# Call the functions
# While loop to continue the program until the user wants to exit

def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer)) 


while True:

    print("A. Addition: ")    
    print("B. Subtraction: ")    
    print("C. Multiplication: ")    
    print("D. Division: ")   
    print("E. Exit")   

    choice = input("Input your choice: ")

    if choice == "a" or choice == "A" :
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a,b)

    elif choice =="b" or choice == "B":
        print("Subtraction")
        a = int(input("Input first number: "))
        b = int(input("Input Second number: "))
        sub(a,b)

    elif choice == "c" or choice =="C":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input Second number: "))
        mul(a,b)

    elif choice == "d" or choice =="D":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input Second number: "))
        div(a,b)

    elif choice == "e" or choice == "E" :
        print("Program Ended")
        quit()