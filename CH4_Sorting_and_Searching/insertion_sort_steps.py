from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt
import numpy as np
import math
    
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

def check_steps(size_of_cabinet):
    cabinet = [int(1000*random.random()) for i in range(size_of_cabinet)]
    global stepcounter
    stepcounter = 0
    sortedCabinet = insertion_sort(cabinet)
    return(stepcounter)


random.seed(5040)
xs = list(range(1, 500))
ys = [check_steps(x) for x in xs]
ys_exp = np.exp(xs)
ys_squared = np.power(xs, 2)
ys_threehalves = np.power(xs, 1.5)
ys_cubed = np.power(xs, 3)
#print(ys)
plt.plot(xs, ys)
axes = plt.gca()
axes.set_ylim([np.min(ys), np.max(ys)+140])
plt.plot(xs, ys_exp)
plt.plot(xs, xs)
plt.plot(xs, ys_squared)
plt.plot(xs, ys_threehalves)
plt.plot(xs, ys_cubed)
plt.title('Comparing insertion sort to other growth rates')
plt.xlabel('Number of files in random cabinet')
plt.ylabel('Steps required to sort cabinet by insertion sort')
plt.show()
