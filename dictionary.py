d={}
n=int(input("enter no of persons "))
for i in range (n):
    name=input("tell the name")
    phone=input("enter phone ")
    d[name]=phone
print(d)
search=input("enter person name to search ")
if search in  d : 
    print(d[search])
else :
    print("does not exist")