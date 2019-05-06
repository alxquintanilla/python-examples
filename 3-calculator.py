
# Function that uses the terminal input for asking numbers
def askNumbers():
    print("Please insert number a: ")
    numA = input()
    print("Please insert number b: ")
    numB = input()
    arr = [int(numA), int(numB)]
    return arr

# This is not in a function is auto executed
print("\n")
print("***************")
print("* Python Calc *")
print("***************")

# This loop will be asking for options 
while True:
    print("\nSelect an operation: \na) Addition, \nb) Substraction, \nc) Multiplication, \nd) Division, \ne) Exit")
    option = str(input())
    if option == "a":
        print("Sum")
        nums = askNumbers()
        print("Result: ", str(nums[0] + nums[1]))
    elif option == "b":
        print("Substraction")
        nums = askNumbers()
        print("Result: ", str(nums[0] - nums[1]))
    elif option == "c":
        print("Multiplication")    
        nums = askNumbers()
        print("Result: ", str(nums[0] * nums[1]))
    elif option == "d":
        print("Division")
        nums = askNumbers()
        print("\n* Result: ", str(nums[0] / nums[1]))
    # if option is invalid then break the while
    else:
        break

print("Bye")



