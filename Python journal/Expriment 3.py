b=int(input("Enter a number:"))
def evenodd(b):
    if b%2==0:
       return True
    else:
        return False
    
if evenodd(b):
    print(f"True-{b} is even")
else:
    print(f"False-{b} is odd")
