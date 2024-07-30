list1=["alok","jitu","Gajendra"]
list2=[2,3,5,12]
print(list1)
print(list2)

######## Negative Indexing#########
print(list2[-2])
print(list2[-1:-1])

############ Positive Indexing #############
print(list2[1])
list3=["alok",22,22.45]
print(list3[2])
print(list1[2])

#### Checking item is present or not

if "jitu" in list1:
    print("jitu  is present ")
else:
    print("Jitu is not present")

############ Jump Index #############
animals = ["dog","lion","cow","goat","elephant","Deer"]
print(animals)
print(animals[1:5])
print(animals[-1:])
print(animals[:-4])
print(animals[:-4])
print(animals[-1:-4])

############ List Comprehension #############
lst= [i for i in range(6)]
print(lst)
lst1=[i for i in range(21) if i%2==0]
print(lst1)

########### List Methods #############
lst = [2,65,13,90,34,51]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
l=[2,34,51,73,20,51]
print(l)
l.reverse()
print(l)
print(l.index(51))
print(l.count(51))
l1=l.copy()
l1[1]=267
print(l)
print(l1)
l.append(310)
print(l)
l.insert(2,1)
print(l)
print(l,l1)
l.extend(l1)
print(l)
l1.extend(l)
print(l1)
l2=["alok",22,12]
l3=["jitu",36,889]
k=l2+l3
print(k)
