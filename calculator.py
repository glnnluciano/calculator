while True:    
    # ask what operation
    operation = input("What operation would you like to perform?\n\nType the word:\n'ADD' for Addition \n'SUB' for Subtraction \n'MUL' for Multiplication \n'DIV' for Division\n\nType Here: ")
    operation = operation.lower().strip()

    operation_list = ["add", "sub", "mul", "div"]
    if operation in operation_list:
        print("\n------------------------------------------------------------\n")
        break
            
    else: 
        print("\n------------------------------------------------------------\n\nInvalid Input. Please choose from the given options.\n")

# ask for num_1 and num_2
while True:
    try:  

        num_1 = float(input("Enter first numbers you'd like to operate.\n\nType Here: ").strip())
        break

    except ValueError:
        print("\nYour input is NOT A NUMBER. Please try again\n\n------------------------------------------------------------\n")

while True:   
    try:

        num_2 = float(input("\nPlease enter second number you'd like to operate.\n\nType Here: ").strip())
        break

    except ValueError:
        print("\nYour input is NOT A NUMBER. Please try again\n\n------------------------------------------------------------")

# print result
# print result for addition
if operation == "add":

    sum_total = num_1 + num_2        

    print("\n------------------------------------------------------------\n\nThe sum of", num_1, "and", num_2, "is", sum_total)

# loop try again
    # ask the user if wants to try again
    # if eys, loop
    # if no, print "Thank You!" and terminate
# add error handling