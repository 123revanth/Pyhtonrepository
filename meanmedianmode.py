size = size + 1

if(size % 2 == 0):
    size = size - 2
    size  = size/2
    sum = list[size] 
    sum = sum + list[size+1]
    median = sum/2
else:
    size = size+1
    size = size/2
    median = list[size]

print(median)
