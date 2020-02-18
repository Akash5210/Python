n=int(input())
factorial=1
if n<0:
    print("Number must be positive")
elif n==0:
    print("factorial=1")
else:
    for a in range(1,n+1):
        factorial=factorial*a

print(factorial)