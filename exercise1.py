def sum_odd(num): 
    
    numbers = [] 
    for number in num: 
        if number % 2 == 1: 
            numbers.append(number)
    return f'The sum is: {sum(numbers)} '

print(sum_odd([3,3,2,10,12]))


