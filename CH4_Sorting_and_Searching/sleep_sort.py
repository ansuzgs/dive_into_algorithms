import threading
from time import sleep

def sleep_sort(i):
    sleep(i)
    global sortedList
    sortedList.append(i)
    return(i)

items = [2, 4, 5, 2, 1, 7]
sortedList = []
ignoreResult = [threading.Thread(target = sleep_sort, args=(i,)).start() for i in items]
