tup1=(1,2,7,"alok")
print(tup1)
print(tup1[-1])
print(len(tup1))
print(tup1[:-2])
if 1 in tup1:
    print("Yes present")
else:
    print("Not present")
tup2=(12,34,23.86)
print(tup1+tup2)
lst=list(tup1)
lst.append("Russia")
print(lst)
lst.pop()
print(lst)
lst[2]="India"
country=tuple(lst)
print(country)

######################## Tuple Methods #####################
tup=(1,23,86,0,12,1)
print(tup.count(1))
print(tup.index(86))
print(len(tup))
