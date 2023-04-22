a = int(input("Enter Your Age : "))
print("Your age is:", a)
print(a>18)
print(a<18)
print(a==18)

if(a>=18):
    print("You are adult")

else:
    print("You are a Boy")

appleprice = 170
budget = 200

if(budget - appleprice > 50):
    print("Buy apple")
elif(budget - appleprice <= 50 and budget >= appleprice):
    print("Considering to buy....")
else:
    print(" Don't buy apple ")



num = int(input())
if(num>0):
    if(num>10):
        if(num>20):
            if(num>30):
                print("greater than 30")
            else:
                print("in the range of 20-30")
        else:
            print("in the range of 10-20")
    else:
        print("number is in the range of 0-10")
else:
    print("the number is negative")