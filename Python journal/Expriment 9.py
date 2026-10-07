print("The given tuples are:")
t1=(1,2,5,7,9,2,4,6,8,10)
print("t1=",t1)
t2=(11,12,13)
print("t2=",t2)
t3=tuple()

print("\na.Print Content of t1 in 2 separate lines:")
print(t1[:5])
print(t1[5:11])
print("\nb.Print even numbers of t1:")
for i in t1:
    if i%2==0:
        t3=t3+(i,)

print(t3)
print("\nc.Concatenate tuple t1 and t2:")

print(t1+t2)
print("\nd.Return maximum and minimum value of t1:")
print("\nMaximum Value of t1 is:")
print(max(t1))
print("\nMinimum Value of t1 is:")
print(min(t1))
