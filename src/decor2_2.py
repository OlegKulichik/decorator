# from functools import wraps

# a = []

def dec (func):
       # a.append(func.__name__)
       # @wraps
       def wrap (*ars, **kwargs):
              print("Работа декоратора вне модуля")
              return(func(*ars, **kwargs))
       return(wrap)


@dec
def func(a):
    print("ds")
    return a ** a



if __name__ == "__main__":
    print(func(2))