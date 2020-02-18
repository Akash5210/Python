n=int(input("Enter the number of rows: "))
#Right pyrimid
for i in range(0,n):
    for j in range(0,n//2+1+1):
        if i<=n//2+1+1:
            print("*",end="")
        else:
            print(" ",end="")
    print("\r")
for i in range(0, n):
    for j in range(0, n // 2 + 1 + 1):
        if i <= n // 2 + 1 + 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("\r")
