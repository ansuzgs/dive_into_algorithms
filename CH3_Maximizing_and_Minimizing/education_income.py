import math
import matplotlib.pyplot as plt

def income(edu_yrs):
    return(math.sin((edu_yrs-10.6)*(2*math.pi/4))+(edu_yrs-11)/2)

def income_derivative(edu_yrs):
    return(math.cos((edu_yrs - 10.6)*(2*math.pi/4))+ 1/2)

xs = [11 + x/100 for x in range(901)]
ys = [income(x) for x in xs]


threshold = 0.0001
MAX_ITER = 10000
current_edu = 12.5
step_size = 0.001
education_change = math.inf

iterations = 0
while((iterations < MAX_ITER) and (abs(education_change) > threshold)):
    education_change = step_size*income_derivative(current_edu)
    current_edu = current_edu + education_change

    if(iterations%10 == 0):
        print(f"[+] Iteration: {iterations}")
        
    iterations = iterations + 1

print(current_edu)

plt.plot(xs, ys)
plt.plot(current_edu, income(current_edu), 'ro')
plt.title('Education and Income')
plt.xlabel('Years of Education')
plt.ylabel('Lifetime Income')
plt.show()