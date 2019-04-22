i=0
count=0
count1=0
while(i!=-1):
    a=input("enter a value:")
    if(a=="x"):
       break
    b=int(a)
    if(b>0):
        count=count+1
    else:
        count1=count1+1
print ("positive value :",count )
print ("negative value :",count1 )
print ("end")             