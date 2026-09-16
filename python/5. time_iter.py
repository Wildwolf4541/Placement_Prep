# import time

# wait_time=1
# max_retries=5
# attempts=0

# while attempts < max_retries:
#     print ("Attempt" , attempts+ 1, "— Wait Time", wait_time)
#     time.sleep(wait_time)
#     wait_time*= 2
#     attempts += 1

dict={"a":1, "b":2}

I=iter(dict)
print(I)
print(next(I))
print(next(I))
print(next(I))