l = [3,2,5,7,3,2,5,3,8,6]
for x in range(len(l)-1):
    for s in range(len(l)-1-x):
        if l[s]>l[s+1]:
            l[s],l[s+1] = l[s+1],l[s]
print(l)