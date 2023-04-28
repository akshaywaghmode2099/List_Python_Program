'''Accept n elements from user and store add elements in seperate
list and even elements in seperate list and display both list

l=[12,33,4,5,6,77,8]
even=[12,4,6,8]
odd=[33,4,77]'''

li=eval(input("Enter list"))

e=[]
o=[]

for val in li:
    if val%2==0:
        e.append(val)
    else:
        o.append(val)

print("even list ",e)
print("odd list ",o)
