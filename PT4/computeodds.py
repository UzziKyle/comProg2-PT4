def totalOdds(num):
    computer = lambda a : 0 if a <= 0 else a + (computer(a-2)) 

    if num % 2 == 0:
        total_value = function(num-1)

    else: 
        total_value = computer(num)
 
    print(total_value)
    return str(total_value)


def function(num):

    odd_numbers = ""
    for n in range(1, (num + 1), 2):
            if (n == num) or (n == num - 1):
                odd_numbers = odd_numbers + str(n)
            else:
                odd_numbers = odd_numbers + str(n) + ", "

    return str(num), odd_numbers, totalOdds(num)