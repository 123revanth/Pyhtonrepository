import random
import statistics

start = int(input("Enter start"))
stop = int(input("Enter stop"))
step = int(input("Enter step"))

x = 0
arr = []

for i in range(0,6):
    x = random.randrange(start,stop,step)
    arr.append(x)
    x = 0

for i in arr:
    print(i,end=" ")

mean = statistics.mean(arr)
median = statistics.median(arr)
mode = statistics.mode(arr)

print("mean:", mean, end=" ")
print("median:", median, end=" ")
print("mode:", mode, end=" ")



