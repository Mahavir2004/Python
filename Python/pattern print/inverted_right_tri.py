row = int(input("Enter the row: "))

for i in range(row,-1,-1):
    for j in range(i):
        print("*",end="")
    print()

