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

