import matplotlib.pyplot as plt

# LCG - Linear Congruential Generator
def next_random(previous, n1, n2, n3):
    next = (previous*n1 + n2) % n3
    return next

def list_random(n1, n2, n3):
    output = [1]
    while(len(output) <= n3):
        output.append(next_random(output[len(output)-1], n1, n2, n3))
    return output

def overlapping_sums(nums, sum_length):
    length_list = len(nums)
    nums.extend(nums)
    output = []
    for n in range(0, length_list):
        output.append(sum(nums[n:(n+sum_length)]))
    return output

print(list_random(29, 23, 32))

overlap = overlapping_sums(list_random(211111, 111112, 300007), 12)
plt.hist(overlap, 20, facecolor='blue', alpha=0.5)
plt.title('Results of the Overlapping sums test')
plt.xlabel('Sum of elements of overlapping consecutive sections of list')
plt.ylabel('Frequency of sum')
plt.show()