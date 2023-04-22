# FOR LOOPS IN PYTHON

name = "Abhishek"

for i in name:
    print(i)


colors = ['red', 'blue', 'green', 'blue', 'yellow']

for i in colors:
    print(i)
    for j in i:
        print(j)

# print numbers upto a certain interval n

n = int(input("Enter the trange :- "))

for i in range(0, n+1):
    print(i)

#increment the sequence with 3:

for i in range(1,n+1,3):
    print(i)