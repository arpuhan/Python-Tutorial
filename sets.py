# st={"alok",12,4.5}
# print(st,type(st))
# for i in st:
#     print(i)
#
# ################## Union and update #####################
s1={1,2,4,5,8,3}
s2={2,54,4,8,12}
# print(s1.union(s2))
# print(s1)
# s1.update(s2)
# print(s1)
# print(s1,s2)

################## intersecion and intersection-update #####################
# print(s1.intersection(s2))
# print(s1)
# print(s2.intersection(s1))
# s1.intersection_update(s2)
# s2.intersection_update(s1)
# print(s1 == s2)

################## symmetric_difference and symmetric_difference_update #####################
# print(s1.symmetric_difference(s2))
# print(s2.symmetric_difference(s1))
# s1.symmetric_difference_update(s2)
# s2.symmetric_difference_update(s1)
# print(s1)

################## difference  and difference_update #####################
# a1={"india","turky","usa"}
# a2={"china","ruse","turky"}
# print(a1.difference(a2))
# print(a2.difference(a1))
# a1.difference_update(a2)
# print(a1)
# a2.difference_update(a1)
# print(a2)

################## set Metchods #####################
city1={"Bbsr","mbj","bpd","bls"}
city2={"bhadrak","mbj","del"}
city={"bhadrak","mbj","del","Bbsr","bpd","bls"}
print(city1.isdisjoint(city2))
print(city.issuperset(city2))
print(city1.issubset(city))
city1.add("tn")
print(city1)
city1.remove("tn")
print(city1)
print(city.pop())
print(city.pop())
print(city)
# del city
# print(city)
city1.clear()
print(city1)
if "mbj" in city2:
    print("mbj is present")
else :
    print("Not present")