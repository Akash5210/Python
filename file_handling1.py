'''
"""File handling example 1"""
import os
file=open("C:/Users/lenovo/Desktop/ak1.txt","w")
file.close()
'''
'''
"""File handling example 2"""
import os
file=open("C:/Users/lenovo/Desktop/ak1.txt",'r')
print(file.read())
file.close()
'''

'''
#File handling example 3
import os
file=open("C:/Users/lenovo/Desktop/ak1.txt",'r')
print(file.read(5))
file.close()
'''
'''
#File handling example 4
import os
file=open("C:/Users/lenovo/Desktop/ak1.txt",'r')
print(file.readline())
file.close()
'''
'''
#File handling example 5
import os
file=open("C:/Users/lenovo/Desktop/ak1.txt",'r')
print(file.readlines())
file.close()
'''
'''
#File handling example 6
import os
file=open("C:/Users/lenovo/Desktop/ak1.txt",'a')
file.write("Currently in Galgorias univerrsity")
file.close()
'''
'''
#File handling example 7
import os
file=open("C:/Users/lenovo/Desktop/ak2.txt",'x')
file.write("Currently in Galgorias univerrsity")
file.close()
'''
'''
#File handling example 8
import os
file=open("C:/Users/lenovo/Desktop/ak2.txt",'x')
file.write("Currently in Galgorias univerrsity")
file.close()
'''
'''
#File handling example 9
import os
os.remove("C:/Users/lenovo/Desktop/a.txt")
'''
'''
#File handling example 10
import os
os.rmdir("C:/Users/lenovo/Desktop/baba")
'''
'''
#deletion of a file using condition
import os
if os.path.exists('C:/Users/lenovo/Desktop/baba'):
    os.rmdir('C:/Users/lenovo/Desktop/baba')
else:
    print("folder not exist")
'''




