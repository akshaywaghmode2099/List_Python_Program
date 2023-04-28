#Accept n nos from user and store cumulative frq into sepearte
#list and display that list

li=eval(input("Enter list "))
cf=[]
sum=0
for val in li:
    sum=sum+val
    cf.append(sum)

print(li)
print("cumulative fre list ",cf)
