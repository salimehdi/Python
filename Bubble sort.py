from array import *
arr = array('i', [8,9,5,1,3,4,2,7])
change = 1
while (change != 0):
    change = 0
    for i in range(len(arr) - 1) :
        if arr[i] < arr[i+1]:
            temp = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = temp
            change += 1
        else:
            break
    
print(arr)
