### Basic 1: print all integers from 0 to 150
for x in range(0,151):
    print(x)

### Multiples of 5
for x in range(0,151,5):
    print(x)

###Counting, the Dojo Way
for x in range (1,101):
        if x%10 ==0:
            print ("Coding Dojo")
        elif x%5 ==0:
            print("Coding")
        else:
            print(x)

### Whoa. That Sucker's Huge
sum = 0
for num in range (1,500000):
    sum = sum + num
print("total is",sum)

###Counting down by 4
for x in range(2018,0,-4):  
    print(x)

###Flexible Counter
lowNum = 2
highNum = 13
mult = 2

for x in range(lowNum,highNum):
    if x % mult ==0:
        print(x)