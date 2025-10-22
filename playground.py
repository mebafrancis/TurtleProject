def add(*args):
    sum1 =0
    for i in args:
        sum1 += i
    print(sum1)

add(1,2,3,4,5)

def calculate(n,**kwargs):
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

calculate(2,add=3, multiply=5)