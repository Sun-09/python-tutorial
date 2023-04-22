
def gmean(a,b):
    a = (a*b)**(0.5)
    return a

def amean(a,b):
    a = (a+b)/2
    return a
def hmean(a,b):
    a = (a*b)/(a+b)
    return a

def add(a,b):     # pass for do nothing
     pass     

if __name__ == "__main__":
    a =20
    b =5
    print("geometric mean of two number %d and %d is : " %(a,b), gmean(a,b))
    print("ariethmetic mean of two number %d and %d is : " %(a,b), amean(a,b))
    print("harmonic mean of two number %d and %d is : " %(a,b), hmean(a,b))