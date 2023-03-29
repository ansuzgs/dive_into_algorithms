import math
import matplotlib.pyplot as plt

def revenue(tax):
    return(100 * (math.log(tax+1) - (tax - 0.2)**2 + 0.04))

def revenue_derivative(tax):
    return(100*(1/(tax+1)-2*(tax-0.2)))

xs = [x/1000 for x in range(1001)]
ys = [revenue(x) for x in xs]

plt.plot(xs,ys)
current_rate = 0.7
plt.plot(current_rate, revenue(current_rate), 'ro')
plt.title('Tax rates and revenue')
plt.xlabel('Tax rate')
plt.ylabel('Revenue')
plt.show()

step_size = 0.001
threshold = 0.0001
MAX_ITER = 10000
rate_change = math.inf

iterations = 0
while((iterations < MAX_ITER) and (abs(rate_change) > threshold)):
    rate_change = step_size*revenue_derivative(current_rate)
    current_rate = current_rate + rate_change

    if(iterations%10 == 0):
        print(f"[+] Iteration: {iterations}")
        
    iterations = iterations + 1


print(current_rate)