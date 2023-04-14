import math

def merge(left, right):
    newCabinet = []
    while( min(len(left), len(right)) > 0 ):
        if left[0] > right[0]:
            to_insert = right.pop(0)
            newCabinet.append(to_insert)
        else:
            to_insert = left.pop(0)
            newCabinet.append(to_insert)

    if(len(left) > 0):
        for i in left:
            newCabinet.append(i)
    if(len(right) > 0):
        for i in right:
            newCabinet.append(i)

    return(newCabinet)

def merge_sort_two_elements(cabinet):
    newCabinet = []
    if(len(cabinet) == 1):
        newCabinet = cabinet
    else:
        left = cabinet[:math.floor(len(cabinet)/2)]
        right = cabinet[math.floor(len(cabinet)/2):]
        newCabinet = merge(left, right)
    return(newCabinet)

def merge_sort_four_elements(cabinet):
    newCabinet = []
    if(len(cabinet) == 1):
        newCabinet = cabinet
    else:
        left = merge_sort_two_elements(cabinet[:math.floor(len(cabinet)/2)])
        right = merge_sort_two_elements(cabinet[math.floor(len(cabinet)/2):])
        newCabinet = merge(left, right)
    return(newCabinet)

def merge_sort(cabinet):
    newCabinet = []
    if(len(cabinet) == 1):
        newCabinet = cabinet
    else:
        left = merge_sort(cabinet[:math.floor(len(cabinet)/2)])
        right = merge_sort(cabinet[math.floor(len(cabinet)/2):])
        newCabinet = merge(left, right)
    return(newCabinet)


#left = [1, 3, 4, 4, 5, 7, 8, 9]
#right = [2, 4, 6, 7, 8, 8, 10, 12, 13, 14]
#newCab = merge(left, right)
#print(newCab)
cabinet = [4,1,3,2,6,3,18,2,9,7,3,1,2.5,-9]
newCab = merge_sort(cabinet)
print(newCab)