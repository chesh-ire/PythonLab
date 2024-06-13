L=[]
a=int(input("enter a number elements "))
for i in range(a):
    elem=int(input("enter elemets "))
    L.append(elem)
print(L)
print(sum(L))
print(len(L))
print(sum(L)/len(L))