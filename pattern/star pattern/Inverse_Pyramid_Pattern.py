n=int(input("Enter the number of rows: "))
#Inverse pyrimid
for i in range(0,n):
    for j in range(0,n*2-1):
        if j<=n*2-2-i and j>=i:
            print("*",end="")
        else:
            print(" ",end="")
    print("\r")