## MATHEMATICAL CALCULATOR

## Create four basic mathematical functions: 'add', 'subtract', 'multiply', and 'divide' that take in two numbers and return the result of the operation.
def ADDITTION(a, b):
    return a + b

def SUBTRACTION(a, b):
    return a - b

def MULTIPLICATION(a, b):
    return a * b

def DIVISION(a, b):
    if b == 0:
        return "Error"
    return a / b

## Create a dictionary 'operations' that assigns the functions to their corresponding operation symbols.
operations = {
    '+': ADDITTION,
    '-': SUBTRACTION,
    '*': MULTIPLICATION,
    '/': DIVISION
}

## Create a function 'calculator' that prompts the user to input the first number.
def calculator():
    num1 = float(input("Enter the first number: "))
    
    should_continue = True
    
## Use a for loop to print the available operation symbols.
    while should_continue:
## Use a for loop to print the available operation symbols.
        print("\nAvailable operations:")
        for symbol in operations.keys():
            print(symbol)
        
        operation = input("Select an operation (+, -, *, /): ")
        
        if operation in operations:
## Prompt the user to input the second number.
            num2 = float(input("Enter the second number: "))
            
## Use the dictionary to retrieve the function that corresponds to the selected operation symbol and store it in a variable 'calculation_function
            calculation_function = operations[operation]
            

            answer = calculation_function(num1, num2)
            
## Print the equation and the result of the calculation.
            print(f"{num1} {operation} {num2} = {answer}")
            
## Ask the user if they would like to continue using the result as the first number for further calculations.
            continue_calculation = input("Would you like to continue with this result as the first number? (yes/no): ").strip().lower()
            
            if continue_calculation == 'yes':
                num1 = answer  
            else:
                should_continue = False  
                calculator() 
        else:
            print("Invalid operation. Please select a valid operation.")

## CALCULATOR FUNCTION
calculator()