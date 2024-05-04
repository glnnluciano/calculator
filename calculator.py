while True:    
    # ask what operation
    operation = str(input("What operation would you like to perform?\n\nType the word:\n'ADD' for Addition \n'SUB' for Subtraction \n'MUL' for Multiplication \n'DIV' for Division\n\nType Here: ").strip())
    operation = operation.lower().strip()

    operation_list = ["add", "sub", "mul", "div"]
    if operation in operation_list:
        break
            
    else: 
        print("\n------------------------------------------------------------\n\nInvalid Input. Please choose from the given options.\n")

# ask for num_1 and num_2
# print result
# loop try again
    # ask the user if wants to try again
    # if eys, loop
    # if no, print "Thank You!" and terminate
# add error handling