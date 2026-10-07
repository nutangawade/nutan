def series_sum(n):
    if n%2==0:
        return -n//2
    else:
        return(n+1)//2
n=int(input("Enter the value of n:"))
print("Sum of series up to{}:{}".format(n,series_sum(n)))
