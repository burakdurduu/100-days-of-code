# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(add(5,5,5,10))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"] 
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=3, multiply=5))


class Car:

    def __init__(self, **kw) -> None:
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make, my_car.model,  my_car.seats, my_car.colour)
