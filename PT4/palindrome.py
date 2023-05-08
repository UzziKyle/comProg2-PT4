def function(input):
    if input == input[::-1]:
        result = "{} is a palindrome.".format(input.title())
        last_letters = input[-3: ]

        return input, result, last_letters
    
    else: 
        result = "{} is not a palindrome.".format(input.title())
        last_letters = input[-3: ]

        return input, result, last_letters
