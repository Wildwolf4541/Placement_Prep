import time

def timer(function):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=function(*args,**kwargs)
        end=time.time()
        print(f"{function.__name__} ran in {end-start} time.")
        return result
    return wrapper

@timer # decorator, timer function se hoke hi example_function call hoga, so time will be calculated.
def example_function(n):
    time.sleep(n)

example_function(2)


def function_details(func):
    def wrapper(*args,**kwargs):
        print(f"Function name: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")
        return func(*args,**kwargs)
    return wrapper

@function_details
def greet(name,greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice",greeting="Hi")  # Output: Hi, Alice!