def square_root(x, y, error_tolerance):
    error = error_tolerance*2
    while(error > error_tolerance):
        z = x/y
        y = (y + z)/2
        error = y*y - x
    return y

print(square_root(5, 1, 0.000000000000001))