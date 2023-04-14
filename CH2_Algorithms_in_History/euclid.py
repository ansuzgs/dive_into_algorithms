def gcd(x,y):
    larger = max(x,y)
    smaller = min(x,y)

    reminder = larger % smaller

    if reminder == 0:
        return(smaller)
    else:
        return(gcd(smaller, reminder))