a1 = {
    'name': 'abc',
    'age': 20,
    'isActive': True
}

print(a1)
print()
key1 = 'name'
val1 = 'xyz'
key2 = 'age'
val2 = 25

d2 = {
    key1 : val1,
    key2 : val2,
    'isActive': True
}
print('d2 values =',d2)
print()
#How to access dictionary
print('d2 key1 value =',d2[key1])
print('d2 key2 value =',d2['age'])
print('d2 isActive value =',d2['isActive'])
print()

#copy and update 
d3 = d2
print('d3 =',d3)
print()
d3['age'] = 30 
print(f'd3 after change age =',d3)
print()
print(f'd2 =',d2)
print()
#use copy method to not change in original data
print('d3 =',d3)
print()
#after use the copy method it will not change the original data.
d4 = d3.copy()
print('d4 =',d4)
print()
print('d3 data =',d3)
print()
d4['age'] = 35
print('change age in d4 =',d4)
print()


empData = [
    {
       'empName':'emp1',
       'age': 24,
       'salary': 25000
    },
    {
       'empName':'emp2',
       'age': 30,
       'salary': 34000
    },
    {
       'empName':'emp3',
       'age': 28,
       'salary': 30000
    },
    {
       'empName':'emp4',
       'age': 35,
       'salary': 25000
    },
    {
       'empName':'emp5',
       'age': 24,
       'salary': 30000,
       'role':['Data analyst','Frontend']
    },
    {
       'empName':'emp6',
       'age': 45,
       'salary': 250000
    },
    {
       'empName':'emp7',
       'age': 40,
       'salary': 75000
    },
    {
       'empName':'emp8',
       'age': 31,
       'salary': 42500
    },
    {
       'empName':'emp9',
       'age': 29,
       'salary': 46200
    }
]

print('empData =',empData)
print()
print('empData = ',empData[4]['role'][1])
