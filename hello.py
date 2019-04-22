n=5
k=n*2-2
for i in range (n):
    for j in range(k):
        print(end=" ")
    k=k-2
    for j in range (2*i+1):
        if (j % 2 == 0):
            print ("6 ", end="")
        else:
            print("1 ", end="")
    print ("")              