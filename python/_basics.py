# from this import that, can be used to import functions, variables, etc.
import random

def chai(n):
    print(n);
chai(1);

# Object/Data Types
# Number, List, Tuple, Set, Dictionary, String, Boolean, None
# random.random(), random.choice([1,2,3,4,5]), random.randint(), random.randrange(1,5)
# random.shuffle(list)
print(random.randint(1, 5)) # Includes both endpoints
print(random.randrange(1, 5)) # Excludes the right endpoint

# -----String----- immutable
username="Akhil Gupta"
print(len(username))
print(username[0]) # First character
print(username[-1]) # Last character
print(username[0:2]) # prints Ak, 2 not included.
print(username[0:6:2])
# username[0] = "a" # Strings are immutable, this will raise an error

# -----List----- mutable
Listt=[102315121,'Akhil',9.54]
print(len(Listt))
print(Listt[0])
Listt[0]=1

# -----Dictionary----- mutable
Dict={'one':'Akhil', 'two':'Divyam', 'three':'Vaibhav'}
print(Dict)
Dict['three']='Ritvik'
print(Dict['three'])

# -----Tuple----- immutable
tup=(1,2,3)
print(len(tup))
#tup[0]=4 will give error.

# -----Set----- mutable
sett={1,2,3,4,5}
sett.add(6)
sett.remove(3)

set1={1,2,3}
set2={3,4,5}

set3=set1.union(set2)  # set1 | set2
set4=set1.intersection(set2)  # set1 & set2
set5=set1.difference(set2)  # set1 - set2
