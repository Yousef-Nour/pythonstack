x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)

#Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)
#In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'

#Change the value 20 in z to 30
z[0]['y'] = 30
print(z)
print("_" * 30)


#iterateDictionary(students)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# def iterateDictionary(students):          ##I can use any way!!
#     for student in students:
#         print(f"first name - {student['first_name']}, last name - {student['last_name']}")
# iterateDictionary(students)

def iterateDictionary(students):
    for student in students:
        for key, value in student.items():
            print(f"{key} - {value}", end=", ")
iterateDictionary(students)
print ("_" * 30)

#Get Values From a List of Dictionaries
# def iterateDictionary2(key_name,students):
#     for student in students:
#         print(student[key_name])
# iterateDictionary2('first_name', students)

def iterateDictionary2(key_name,other_list):
    for i in other_list:
        print(i[key_name])
iterateDictionary2('last_name', students)    # i can change to first_name
print ("_" * 30)
#Iterate Through a Dictionary with List Values

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for key, value in dojo.items:
        print(f"{key} {values}")
        for value in values:
            print(value)
        
    printInfo(dojo)


