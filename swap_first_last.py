#Accept list from user and swap 1st and element in a list
#and display list
'''
li=eval(input("Enter list "))

print(li)
print("After swapping fisrt and last element")
li=li[-1:]+li[1:-1]+li[0:1]
print(li)
'''

li=eval(input("Enter list "))
li[0],li[-1]=li[-1],li[0]
print("After swapping fisrt and last element")
print(li)
