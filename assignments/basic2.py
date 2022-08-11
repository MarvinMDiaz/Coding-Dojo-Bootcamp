
#######CountDown#####
def countdown(num):
    list1 = []
    for x in range (num,-1,-1):
        list1.append(x)
    return list1
print (countdown(8))

####Print and return####
def p_r(num1,num2):
    emptylist = []
    emptylist.append(num1)
    emptylist.append(num2)
    print(emptylist[0])
    return emptylist [1]
print(p_r(4,5))

####first plus length###
def plusLength(list):
    result =list[0] + len(list)
    return result
print(plusLength([4,2,3,4,5,10,7]))

###Greater than Second###
def greater(list):
    if len(list)< 2:
        return False
    newList = []
    for x in list:
        if x > list[1]:
            newList.append(x)
    return newList
            
    

print(greater([1,3,4,4,5,6]))
print(greater([8]))

####Length, That Value####
def sizeValue(size,value):
    newList = []
    for x in range(size):
        newList.append(value) 
    return newList
print(sizeValue(12,3))
