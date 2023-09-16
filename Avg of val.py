dist = {}
num = int(input("Number of elements is dist : "))
for i in range(num):
    num1 = int(input("Enter Key : "))
    num2 = int(input("Enter Value : "))
    dist.update({num1:num2})
    
count = 0
sum = 0
for i in dist.keys():
    sum+=dist[i]
    count+=1
print("Average is ",(sum/count))
