
#Accept list from user and also accept search element
#if element is present then display it's first occurance

'''l=[12,33,44,55,33,5,33,78]
search ele=33
first occurance =1

search ele=330
o/p element is not present
'''

li=eval(input("enter the list"));
se=int(input("enter the search ele"))
'''cnt=0
for i in range(0,len(li)):
    if li[i]==se:
        cnt=cnt+1
        break

if cnt>0:
    print("First occurance ",i)
else:
    print("element not found")
'''
if se in li:
    print("first occurance ",li.index(se))
else:
    print("element not found ");
