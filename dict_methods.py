student = {
    'name': 'stud',
    'age': 21,
    'stream': ['Science','Commerce'],
    'address': 'add1',
    'cont_info':{
         'mob_no': 245634,
         'email': 'abc@gmail.com'
    }

}
print('student = ',student)
print('stream =',student['stream'][0])
print()
print('mob =',student['cont_info']['email'])
print()
#Get method
#This method get the specified values
print('apply get method =',student.get('cont_info'))
print()

#Update method
#this method update new elements in the dictionary
student.update({'nationality': 'India'})
print('apply update method =',student)
print()

# keys method
# It returns the keys name in the dictionary
print(f'apply key method = {list(student.keys())}')
print(f'apply key method =',student.keys())
print()

#Items method
#This method pairs the dictionary key and values
print('student =',student)
print()
#student.items()
print('apply item method =',student.items())
print()

#Values method
#It return the value of the key
#student.values()
print('apply values method =',student.values())
print()

info = {
    'name': 'abc',
    'age': 30,
    'gender': 'male'
}
#Setdefault method
#This method return the value of the specified if the key is not present then it will insert the key 
print('info = ',info)
print()
info.setdefault('age',50)
print('apply setdefault method = ',info)
print()
info.setdefault('city','Nagpur')
print('apply setdefault method = ',info)
print()


