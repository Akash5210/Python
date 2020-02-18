from math import sqrt

n=int(input("Enter the maximum Number: "))


for j in range(3,n):
    for k in range(j+1,n):
        p=j**2 + k**2
        if sqrt(p) in range(5,21):
            print(j,k,int(sqrt(p)))
