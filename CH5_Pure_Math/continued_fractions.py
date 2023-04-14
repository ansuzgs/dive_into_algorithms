import math


def continued_fractions(x,y, length_tolerance):
    output = []
    big = max(x,y)
    small = min(x,y)

    while(small > 0 and len(output) < length_tolerance):
        quotient = math.floor(big/small)
        output.append(quotient)

        new_small = big % small
        big = small
        small = new_small

    return(output)

def get_number(continued_fraction):
    index = -1
    number = continued_fraction[index]

    while(abs(index) < len(continued_fraction)):
        next = continued_fraction[index-1]
        number = 1/number + next
        index -= 1
    
    return(number)

def continued_fraction_decimal(x, error_tolerance, length_tolerance):
    output = []
    first_term = int(x)
    leftover = x - first_term
    output.append(first_term)
    error = leftover
    while(error > error_tolerance and len(output) < length_tolerance):
        next_term = math.floor(1/leftover)
        leftover = 1/leftover - next_term
        output.append(next_term)
        error = abs(get_number(output) - x)
    return(output)

x = 105
y = 33

continued_fraction = continued_fractions(x,y,10)

print(continued_fraction)
print(get_number(continued_fraction))

x = 1.4142135623730951
print(continued_fraction_decimal(x, 0.00001, 10))