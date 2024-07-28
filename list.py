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