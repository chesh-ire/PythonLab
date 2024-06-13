num = int(input("enter a number "))
for i in range (2,num,1):
    if(num%1==0):
       print("not")
    break
if(i==num-1):
    print("is")