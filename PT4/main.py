try:
    print("1 || Compute Total Odds\n2 || Palindrome\n3 || Exit")
    input_module = int(input("Enter module number: ").strip())

    if input_module == 1:
        from computeodds import function

        user_input = int(input("\nEnter a number: ").strip())

        result = function(user_input)

        file = open("Compute_Total_Odd.txt", "w")
        file.write("Input: {}\n\nOdd Numbers: {}\n\nTotal: {}".format(result[0], result[1], result[-1]))
        file.close()

        file = open("Compute_Total_Odd.txt", "r")
        print("\n" + file.read())
        file.close()


    elif input_module == 2:
        from palindrome import function
        
        user_input = input("\nEnter any number or word: ").strip().lower()
        
        result = function(user_input)

        file = open("Palindrome.txt", "w")
        file.write("Input: {}\n\n{}\n\nThe last three characters are {}.".format(result[0],result[1],result[2]))
        file.close()

        file = open("Palindrome.txt", "r")
        print("\n" + file.read())
        file.close()

    elif input_module == 3:
        quit()

    else: 
        print("\nInvalid input.")


except ValueError:
    print("\nInvalid input.")