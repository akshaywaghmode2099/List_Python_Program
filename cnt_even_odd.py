#Accept list from user and count no of even and odd elements in a list


li=eval(input("Enter list"))
even=0;
odd=0

for val in li:
    if val%2==0:
        even=even+1
    else:
        odd=odd+1

print("no of even elements ",even)
print("no of odd elements ",odd)
