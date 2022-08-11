##1
x = [ [5,2,3], [10,8,9] ] 

x[1][0]= 15
print(x)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},  
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'], 
                    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]

z[0]['y']= 30
print(z)


####2
students2 = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]



def iterateDictionary(some_list):
    for x in some_list:
        for k, v in x.items():
            print(f'{k} - {v}')
iterateDictionary(students2)

####3
students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDict2(key_name,some_list):

    for x in some_list:
        if key_name == 'first_name':
            print (x[key_name])
        else:
            if key_name == 'last_name':
                print (x[key_name])
            

print(iterateDict2('first_name',students))
print(iterateDict2('last_name',students))

###Iterate Through a Dictionary with List Values

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def info(dict1):

    for key,value in dict1.items():
        print(f'{len(value)}, {key} ')
        for x in value:
            print(x[0:])


print(info(dojo))
