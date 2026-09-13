food_varities={"dosa":"South", "pasta":"Italy", "lassi":"Punjab"}

print(f"{food_varities["dosa"]}\n")
food_varities["dosa"]="South-india"
food_varities["rasgulla"]="West-Bengal"

# for i in food_varities:
#     print(i, food_varities[i])
for key, value in food_varities.items():
    print(key, value)


food_varities.pop("rasgulla") # for specific
food_varities.popitem() # for last

food_varities_copy=food_varities.copy()

squared_nums = {x:x**2 for x in range(11)}
print(squared_nums)
squared_nums.clear()


keys=["Akhil","Divyam","Abhinav"]
default_value="Present"

dictt= dict.fromkeys(keys,default_value)
print(dictt)
print(dict.fromkeys(keys,keys))


# Nested-> {{},{},{}}
tea_shop={
    "tea": {"Masala":"Spicy","Ginger":"Zesty","Lemon":"Healthy"},
    "coffee": {"Latte":"Milky","Espresso":"Strong"},
}
print(tea_shop["tea"])
print(tea_shop["tea"]["Masala"])