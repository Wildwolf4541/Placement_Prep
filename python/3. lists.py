tea_varities=["Black", "Green", "White", "Oolong"]
print(tea_varities)
print(tea_varities[0])
print(tea_varities[-1])

tea_varities[3]="Herbal"
tea_varities[1:3]=["Green","Masala"]
print(tea_varities)

tea_varities[1:1]=["White","Oolong"] #kind of insert
print(tea_varities)

tea_varities[1:2]=[] #kind of delete
print(tea_varities)

for i in tea_varities:
    print(i, end=" ") # by default endl

if "White" in tea_varities:
    print("White is present.")
else:
    tea_varities.append("White") #adds to the list at last
    print(f"\nAppended List: {tea_varities}")

tea_varities.pop() #removes last from list
tea_varities.remove("Oolong") # removes specific
tea_varities.insert(1,"Matka") #adds at specific position

print(tea_varities)


tea_varities_copy= tea_varities.copy() # different references in memory.
tea_varities_copy.append("lemon")
print(tea_varities_copy)
print(tea_varities)

squared_nums= [x**2 for x in range(11)]
print(f"\n{squared_nums}")

# Nested-> [[],[],[]]