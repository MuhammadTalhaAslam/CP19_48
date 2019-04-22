i=0
while(i!=-1):
    a=input("enter a value:")
    if(a=="x"):
        break
    b=int(a)
    if((b**0.5)**2==b):
        print (b**0.5,"is the perfect square of :",b)
    else:
        print("not a perfect square")
print ("end")                