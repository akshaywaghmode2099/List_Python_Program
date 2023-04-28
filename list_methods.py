'''l=[1,3,4,55,6,777,88,56,6789.5]
print(l)
print(len(l))
print("max ele ",max(l))
print("min ele ",min(l))
max=l[0]
for ele in l:
    if ele>max:
        max=ele


l=['java','php','cpp','c prog']
print(l)
print("max ele ",max(l))
print("min ele ",min(l))

l=['java','php','cpp','c prog',45,99,100]
print(l)
print("max ele ",max(l))
print("min ele ",min(l))
'''
'''str='python'
str.upper()
print(str)

l=[10,20,30,50]
l.append(800)
print(l)

l=[10,20,30,50]
l2=[90,987]
l.append(l2)    #[10, 20, 30, 50, [90, 987]]
print("using append ",l)


l=[10,20,30,50]
l2=[90,987]
l.extend(l2)    #[10, 20, 30, 50, 90, 987]
print("using extend ",l)



l=[5,6,7,80,90,8,9,8,5]
print("count ",l.count(8))
print("index of 8 ",l.index(8))
# print("index of 800 ",l.index(8)) Error

l=[1,2,66,7]
l.insert(10,12) #inavlid index
print("insert ",l)  #add ele at the end

l=[100,200,500,600,800]
print(l)
l.pop()     #pop last ele
l.pop(56)   #invalid index 
print("After pop ",l)   #Error




l=[1,2,3,4,5,4,5,6,5]
print(l)
print(l.remove(5))
print("After remove 5 ",l)
l.remove(900)   #invalid element
print(l)        #Error


l=[10,30,44,78,65]
l.reverse()
print("Reverse list ",l)




l=[10,30,44,78,65]
l.sort()    #sort list ascending
print(" ascending list ",l)


l=[10,30,44,78,65]
l.sort(reverse=True)    #sort list descending
print("descending list ",l)

'''

l1=[10,20,30]
l2=l1
l1.append(100)
print(l2)


l1=[10,20,30]
l2=l1.copy()
l1.append(100)
print(l2)


























