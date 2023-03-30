from timeit import default_timer as timer
    
def insert_cabinet(cabinet, to_insert):
    check_location = len(cabinet) - 1
    insert_location = 0
    global stepcounter

    while(check_location >= 0):
        stepcounter += 1
        if(to_insert > cabinet[check_location]):
            insert_location = check_location + 1
            check_location = -1
        check_location = check_location - 1
    stepcounter += 1
    cabinet.insert(insert_location, to_insert)
    return(cabinet)

def insertion_sort(cabinet):
    newCabinet = []
    global stepcounter
    while len(cabinet) > 0:
        to_insert = cabinet.pop(0)
        stepcounter += 1
        newCabinet = insert_cabinet(newCabinet, to_insert)
    return(newCabinet)

cabinet = [8,4,6,1,2,5,3,7]
stepcounter = 0
start = timer()
sortedCabinet = insertion_sort(cabinet)
end = timer()
print(f"[+] Sorting steps: {stepcounter}")
print(f"[+] Sorting time: {end-start}")
print(f"[+] Sorted list: {sortedCabinet}")