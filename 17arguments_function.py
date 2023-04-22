# Different types of Arguments

# 1. Default Argument


def average(a=9, b =1):
    print("Average : ", (a+b)/2)

average()
average(5) #5+1/2
average(b=3) #9+3/2

# 2. Required Argument

def add(a,b):     
     print("Sum is : ",a+b)   

add(4, 6)


# 3. Keywords Argument

average(b=8, a=34)  #not necessary to give in order


# 4. Keyword Arbitary Arguments

def multiplication(*numbers):
     mul = 1
     for i in numbers:
          mul = mul* i
     print("The multiplication is : ", mul)


multiplication(3,9)