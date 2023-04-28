#Accept list from user and also accept search element
#if element is present then display it's last occurance

'''l=[12,33,44,55,33,5,33,78]
search ele=33
first occurance =6

search ele=330
o/p element is not present'''


'''li=eval(input("enter the list"));
se=int(input("enter the search ele"))
cnt=0
for i in range(0,len(li)):
    if li[i]==se:
        pos=i;
        cnt=cnt+1
    

if cnt>0:
    print("last occurance ",pos)
else:
    print("element not found")
'''






li=eval(input("enter the list"));
se=int(input("enter the search ele"))

for i in range(len(li)-1,-1,-1):
    if li[i]==se:
        print("last occurance ",i)
        break
else:
    print("element not found")











    
