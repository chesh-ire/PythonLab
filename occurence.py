d={}
str=input("enter string ")
for ch in str :
    d[ch]=d.get(ch,0)+1
print(d)

for i in d : 
    print(i,":",d[i])
