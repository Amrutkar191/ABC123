import time
import random
def partition(a, left, right):
    i = left - 1
    pivot = a[right]
    
    print(f"Choosing pivot {pivot}:")
    
    for j in range(left, right):
        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    
    a[i + 1], a[right] = a[right], a[i + 1]
    
    return (i + 1)

def quick(a, left, right):
    if left < right:
        p = partition(a, left, right)
        
        quick(a, left, p - 1)
        quick(a, p + 1, right)

random.seed(1)
n = 100
unique_values = set()
while len(unique_values) < n:
    unique_values.add(random.randint(1, 1000))
a = list(unique_values)

print("Original array:", a)
start_time = time.time()
quick(a, 0, len(a) - 1)
end_time = time.time()
print("After quick sorting, output array =", a)
print(f"Execution time: {end_time - start_time} seconds")
