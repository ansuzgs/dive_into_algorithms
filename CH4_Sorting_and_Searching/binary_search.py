import math

sortedCabinet = [1,2,3,4,5,6,7,8,9,10]

def binary_search(sortedCabinet, looking_for):
    guess = math.floor(len(sortedCabinet)/2)
    upperbound = len(sortedCabinet)
    lowerbound = 0

    while( sortedCabinet[guess] != looking_for ):
        if(sortedCabinet[guess] > looking_for):
            upperbound = guess
            guess = math.floor((guess + lowerbound)/2)
        if(sortedCabinet[guess] < looking_for):
            lowerbound = guess
            guess = math.floor((guess + upperbound)/2)
    
    return(guess)

def binary_search_recursive(sortedCabinet, looking_for, low, high):
    if(low > high):
        return False
    else:
        mid = math.floor((low + high)/2)
        if(sortedCabinet[mid] == looking_for):
            return(mid)
        elif(sortedCabinet[mid] > looking_for):
            return( binary_search_recursive(sortedCabinet, looking_for, low, mid-1) )
        else:
            return( binary_search_recursive(sortedCabinet, looking_for, mid+1, high) )

print(binary_search(sortedCabinet, 8))
print(binary_search_recursive(sortedCabinet, 8, 0, len(sortedCabinet)))
