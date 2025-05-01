l=[('bread',80),('butter',50),('cheese',100)]
for i in range(3):
    for j in range(i+1):
        if l[i][1]<l[j][1]:
            l[i],l[j]=l[j],l[i]
print(l)       
