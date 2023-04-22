for i in range(12):
    print("5 x %d = " %i, 5*i)
    if(i==10):
        break    #breaks the loop when i becomes 10

print("nikal gaya loop se jab i == ", i)


for i in range(12):
    if(i==10):
        print("skip the content")
        continue
    print(" 5 X ",i," = ", 5*i)