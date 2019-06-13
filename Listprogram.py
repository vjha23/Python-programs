adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
list1=[]
list2=[]
print("no thst are greater than 5")
for i in adhoc:
    if i > 5:
        print(i,",",end="")
        list1.append(i)
print("no that are less than and equal 2")
for i in adhoc:
    if i<=2:
        print(i,",",end="")
        list2.append(i)

print('\n\n')
print([list1])
print([list2])
