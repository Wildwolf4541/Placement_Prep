password= input("Enter Password: ")
count=len(password)
ptype=""
if count<6:
    type="Weak"
elif count<10:
    type="Medium"
else:
    type="Strong"

print(f"Your password strength is: {type}")


# for i in range(0,len(nums)-1,1):
tablee=input("Enter number: ")
table=int(tablee)
for i in range(1,11):
    if(i%5!=0):
        mul=table*i
        print(f"{table} * {i} = {mul}")


numm= input("Enter a number: ")
num=int(numm)
while num<1 or num>10:
    numm=input("Enter a number: ")
    num=int(numm)

print("Escaped the Matrix.")