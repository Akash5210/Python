n=int(input("Enter the number of rows: "))
#pyrimid
for i in range(0,n):
    for j in range(0,n*2-1):
        if j<=n-1+i and j>=n-1-i:
            print("*",end="")
        else:
            print(" ",end="")
    print("\r")

