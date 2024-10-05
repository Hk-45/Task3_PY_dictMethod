l1 = [15,1,4,65,200,7,-5,2.3,-1,89,100,5.4]

print(f'original list data',l1)
print()
#apply sort method
l1.sort()
print('l1 after sort',l1)
print()
#reverse sort
l1.sort(reverse=True)
print('l1 reverse sort',l1)

print()
l2 = ['abc','xyz',5]

print(f'original data= {l2}')
#append method
#append method create new index and the append value.
print()
l2.append('newStr')
print(f'apply append method',l2)
print()
#Insert method
#this method add values on the specified position.
l2.insert(2,'addNew')
print('apply insert method',l2)
print()
#Remove method
#In this method we give the value that present in the list data for removing data.
#If we give the index position it will not work.
l2.remove(5)
print('apply remove method',l2)
print()
#del method
#In this method we give the index position for removing the list data.
del l2[3]
print('apply del method',l2)
print()

l3 = ['abc',2,5,4,88,100,452,6,78,150,400,50,501,23,41,50,80,45,62,30,44,22,'xyz']

l4 = l3.copy()
print(f'original list data= {l3}')
print()
print('copy in l4',l4)
print()
#Clear method
# This method removes all the data from the list.
l4.clear()
print('l4 Data=',l4)
print()
print('apply clear method=',l4)
print('l3=',l3)
print()
#again copy the data 
l4 = l3.copy()
print('l4=',l4)
print()
#Count method
# This method is used to count the elements comes how many times in list
countValue = l4.count(5)
print('apply count method=',countValue)
print()
print('apply count method [5]=',l4.count(5))
print()
print('apply count method [50]=',l4.count(50))
print()

#Extend method
#This method is add the specified list elements to other list
laptop = ['HP','Dell','Lenovo','Mac','Gaming laptops']
bike = ['pulsar','hero honda','yamaha']

print('laptop list = ',laptop)
print()
print('bike list =',bike)
print()
bike.extend(laptop)
print('apply extend method, add laptop list into bike list = ',bike)
print(bike)
print()

#index method 
#This method find index position of the value or element
print('l4 list = ',l4)
print()
print('apply index method = ',l4.index("xyz"))
print()

#pop method
print('l4 list =',l4)
print()
l4.pop(2)
print('apply pop method = ',l4)
print()
print('apply pop = ',l4.pop(1))