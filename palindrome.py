str=input("enter string ")
count =0
for ch in str: 
  count=count+1
  print(count)
rev=str[::2]
if(rev==str):
   print("is")
else:
   print("not")