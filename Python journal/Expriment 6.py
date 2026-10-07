string1=input("Enter a first String:")
string2=input("Enter a second String:")
indices=[]
i=0

while i<=len(string1)-len(string2):
    if string1[i:i+len(string2)]==string2:
        indices.append(i)

        i+=1
    else:
        i+=1

if indices:
    print(indices)
else:
    print(-1)
    
    
 
