# # create a function that takes 2 numbers and MULTIPLIES them, retuning the result
# def multiply(num1, num2):
#     return int(num1 * num2)
# # create a function that takes 2 numbers and DIVIDES the second from the first, returning the result
# def divide(num1, num2):
#     return int(num1 / num2)
# # create a function that takes 2 numbers and ADDS them, returning the result
# def add(num1, num2):
#     return int(num1 + num2)
# # create a function that takes 2 numbers and MINUSES the second from the first, returning the result
# def minus(num1, num2):
#     return int(num1 - num2)
#
#
# # FUNCTION CALLS
# print(multiply(20, 5))
# print(divide(1000, 10))
# print(add(65, 35))
# print(minus(147, 47))
# # each of the above functions should print 100 as on INTEGER
#
# # Extension:
# # How can you make your calculator more useful?
#
# # How can you make the output more informative

# Program make a simple calculator

# This function adds two numbers
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def power(x, y):
    return x ** y
while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            if num2 == 0:
                print("Invalid Input")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "^", num2, "=", power(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break

    else:
        print("Invalid Input")


