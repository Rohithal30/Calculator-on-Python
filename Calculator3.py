# empliment a History function
 
last_calculation = []

def rec_history(result):
  last_calculation.append(result)

def history():
  global last_calculation
  if last_calculation == []:
    print("No past calculations to show")
  else:
    for x in last_calculation:
        print(x)

# Define functions for arithmetic operations

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("float division by zero")
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

def remainder(num1, num2):
    return num1 % num2

# Define function to select the appropriate math function based on user input

def select_op(choice):
    if choice == "#":
        return -1

    elif choice == "$":
        return 0

    elif choice in ('+','-','*','/','^','%'):
        while True:
            num1s = str(input("Enter First Number: "))
            print(num1s)
            
            if num1s.endswith("#"):
                return -1

            if num1s.endswith("$"):
                return 0

            try:
                num1 = float(num1s)
                break

            except:
                print("Not a valid number,please enter again")
                continue   

        while True:
            num2s = str(input("Enter Second Number: "))
            print(num2s)

            if num2s.endswith("#"):
                return -1

            if num2s.endswith("$"):
                return 0

            try:
                num2 = float(num2s)
                break

            except:
                print("Not a valid number,please enter again")
                continue  

        result = 0.0
        last_calculation = ""
        if choice == '+':
            result = add(num1, num2)
  
        elif choice == '-':
            result = subtract(num1, num2)
  
        elif choice == '*':
            result = multiply(num1, num2)
  
        elif choice == '/':

            if num2 == 0:
                print("float division by zero")
                result = "None"

            else:
                print(num2)
                result = divide(num1, num2)

    
        elif choice == '^':
            result = power(num1, num2)
        
        elif choice == '%':
            result = remainder(num1, num2)
        
        else:
            print("Something Went Wrong")


        last_calculation =  "{0} {1} {2} = {3}".format(num1, choice, num2, result) 
        print(last_calculation )
        rec_history(last_calculation)

    elif choice == '?':
        history()

    else:
        print("Unrecognized operation")


# This is the main loop.
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("9.History  : ? ")

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  if(select_op(choice) == -1):
    # program ends here
    print("Done. Terminating")
    exit()