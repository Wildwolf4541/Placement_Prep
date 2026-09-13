uname='Akhil Gupta'
print(uname[0:7:2])
print(uname.lower())
print(uname.upper())
print(uname.replace("Akhil","Sandeep"))
print(uname.find("Gupta"))
print(uname.count("Gupta"))
print("Akhil" in uname) # returns true or false

spaces="    Akhil    "
print(spaces.strip()) # removes extra spaces.

chai="Lemon, Ginger, Masala, Mint"
print(chai.split()) # splits on spaces and converts in list
print(len(chai.split(", "))) # splits on ", " and does not includes these. len gives len of list.

chai_list=["Lemon", "Ginger", "Masala", "Mint"]
print(", ".join(chai_list)) # join converts list to string.


chai_type="Masala"
quantity=2
order="I ordered {} cups of {} chai."
print(order.format(quantity,chai_type))


quote= "He said, \"I am Akhil Gupta\". " # to use "" in strings
print(quote)
quote2= r"Akhil\nGupta" # raw string
print(quote2)