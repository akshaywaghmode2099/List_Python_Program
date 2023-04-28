#Accept list from user and print list in reverse order

li=eval(input("Enter list "))
print("list in reverse order ")
for i in range(len(li)-1,-1,-1):
    print(li[i],end=" ")
