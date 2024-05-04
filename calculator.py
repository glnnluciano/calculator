def calculator():
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

    # print result for subtraction
    elif operation == "sub":

        difference = num_1 - num_2

        print("\n------------------------------------------------------------\n\nThe difference of", num_1, "and", num_2, "is", difference)

    #print result for multiplication
    elif operation == "mul":

        product = num_1 * num_2

        print("\n------------------------------------------------------------\n\nThe product of", num_1, "and", num_2, "is", product)

    #print result for division
    elif operation == "div":

        try:
            quotient = num_1 / num_2

            print("\n------------------------------------------------------------\n\nThe quotient of", num_1, "and", num_2, "is", quotient)

        except ZeroDivisionError:
            print("\n------------------------------------------------------------\n\nError. Your second number/divisor is 0.")

# loop to try again
while True:

    calculator()

    while True:

        # ask the user if wants to try again
        user_try_again = input("\nDo you want to try again? y/n\n\nType Here: ")

        # if yes loop
        if user_try_again.lower() == "y":
            print("\n")
            break

        # if no, break, print "Thank You!" and terminate
        elif user_try_again.lower() == "n":
            end_of_program = "Thank You!"
            print("\n------------------------------------------------------------\n", end_of_program.center(55, " "),"\n------------------------------------------------------------\n")
            exit() 
        
        # else, invalid input
        else:
            print("\n------------------------------------------------------------\n\nInvalid Input. Please choose from the given options.")
