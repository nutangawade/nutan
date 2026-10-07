import numpy as np

print("""----NumPy Operation Menu---
    1.Create an array filled with 1's.
    2.Find maximum and minimum values from an array.
    3.Dot product of 2 array.
    4.Peshape a 1-D array to 2-D array.
    5.Exit.""")

while True:
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        r=int(input("Enter rows:"))
        c=int(input("Enter columns:"))
        a=np.ones((r,c),int)
        print("Array of 1's :\n",a)
              
    elif choice==2:
        arr=np.array([9,7,1,2,3,8,4,5,6])
        print(arr)
        print("Maximum Element=",np.max(arr))
        print("Minimum Element=",np.min(arr))
    elif choice==3:
        a=np.array([[1,2],[4,5]])
        b=np.array([[7,8],[10,11]])
        print("First Array:",a)
        print("Second Array:",b)
        print("Dot Product=",np.dot(a,b))
    elif choice==4:
        arr=np.array([1,2,3,4,5,6,7,8])
        print(arr)
        r=int(input("Enter rows:"))
        c=int(input("Enter columns:"))
        new=arr.reshape(r,c)
        print("Reshaped Array:\n",new)
    elif choice==5:
        print("Exiting...")
        break
    else:
        print("Invalid Chioce! Please enter 1-5.")
              
    
