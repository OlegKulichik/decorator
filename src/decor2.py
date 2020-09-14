from decor2_2 import dec as dc


def decorator(value):
       def wrapp1 (func):
              def wrapp2(*args,**kwargs):
                  wrapp2.var += 1
                  if wrapp2.var == 1:
                         print(value)
                  return func(*args,**kwargs)
              wrapp2.var = 0
              return wrapp2
       return wrapp1


@dc
@decorator("Декоратор для 1")
def func1(x):
       return x

func1(3)


@decorator("Декоратор для 2")
def func2(x):
       return x

func2(1)
func2(2)
func2(3)
func2(4)

@decorator("Декоратор для 3")
def func3(x):
       return x

func3(1)
func3(2)
func3(3)

@decorator("Декоратор для 4")
def func4(x):
       return x

func4(1)
func4(2)
func4(3)
func4(4)

@decorator("Декоратор для 5")
def func5(x):
       return x

func5(1)
func5(2)
func5(3)
func5(4)
func5(5)

@decorator("Декоратор для 6")
def func6(x):
       return x

func6(1)
func6(2)
func6(3)

print(
#     "Количество вызовов функции func1: {} раз(а)\n"
    "Количество вызовов функции func2: {} раз(а)\n"
    "Количество вызовов функции func3: {} раз(а)\n"
    "Количество вызовов функции func4: {} раз(а)\n"
    "Количество вызовов функции func5: {} раз(а)\n"
    "Количество вызовов функции func6: {} раз(а)".format(func2.var,func3.var,func4.var,func5.var,func6.var)
)

# a = [1,2,3,4,5,18]


# v = list(filter(lambda x: x>2 , a))
# c = list(map(lambda x: x*2 , a))
# print(c,v)