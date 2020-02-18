travelling=input("Enter yes or no:\n")

while travelling=="yes":
    a=int(input("Enter no. of passangers:"))
    for b in range(1,a+1):
        name=input("Name: ")
        age=int(input("Age: "))
        sex=input("sex: ")
        print(name)
        print(age)
        print(sex)
    travelling="no"