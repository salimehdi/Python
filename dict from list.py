lst = [2,2,2,2,2,3,3,4,4,4,4,4,4,5,5,5]
dist = {}
for i in lst:
    if i in dist.keys():
        dist[i]+=1
    else:
        dist.update({i:1})
print (dist)
