#Accept list from user and sum of even elements in given list


li=eval(input("Enter list"))
sum=0
for v in li:
    if v%2==0:
        sum=sum+v

print("sum of even elements ",sum)
