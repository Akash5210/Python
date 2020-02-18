#array application
import array as arr

a=arr.array('i',[1,2,8,4,-5,6])
print(a)                                #for printing of array
print(a[1])                             #for array addressing
print(len(a))                           #for array length

for i in a:                             #loop in array
    print(i)

a.append(7)                            #adding array element
print(a)
a.extend([8,9,10])
print(a)
a.insert(2,-2)
print(a)


a.pop(2)                                #deletion of array
#a.remove(7)
print(a)

c=a[0]                                  #substitution of value
a[0]=a[1]
a[1]=c
print(a)

print("---------------------------------------------")

b=arr.array('d',[3.7,8.7])               #array concatenation
c=arr.array('d',[1.1,2.1,3.1,2.6,7.8])
d=arr.array('d')
d=b+c
print("New array d=",d)

print("----------------------------------------------")

print(a)
print(a[::-1],"\n",a)               #reverse copy of array will be formed
print(a[0:5])                       #slicing

print("-----------------------------------------------")

print(a)

for i in a:                         #for loop
    print(i)

i=0
while i<len(a):                     #while loop
    print(a[i])
    i=i+1

print("---------------------------------------------")

list1=[10,20,30]                   #identity operator
list2=[10,20,30]
x=list1
print(x is list1)
print(list1 is list2)
print(list1 is list1)
print(list1 is not list2)

print(10 in list1)                 #membership operator
print(a in list1)
print(40 not in list1)
print("---------------------------------------------")

