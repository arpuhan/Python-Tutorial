info={216:"id","name":"alok","occ":"student","age":21}
print(info,type(info))
print(info["name"])

################## Accessing Dictionary Items #################
print(info[216])
print(info.get("age"))
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"The value of {key} is {info[key]}")
print(info["name"])
