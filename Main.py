dict_info={"name":"Ayo","age":"15", "place":"Ireland",}
print(dict_info)

names=["Ayo", "John", "Alex"]
print(names[1])

print(dict_info.keys())

print(dict_info.values())


for key in dict_info:
    print(key)

for value in dict_info.values():
    print(value)


for key, value in dict_info.items():
    print(key, value)

dict_info["Hobby"]="Gaming"
print(dict_info)

del dict_info['age']
print(dict_info)



