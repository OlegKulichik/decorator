def decorator(func):
       def wrapper(*args,**kwargs):
           wrapper.var += 1
           return func(*args,**kwargs)
       wrapper.var = 0
       return wrapper

@decorator
def func1(x):
       return x

func1(3)

@decorator
def func2(x):
       return x

func2(1)
func2(2)
func2(3)
func2(4)

@decorator
def func3(x):
       return x

func3(1)
func3(2)
func3(3)

@decorator
def func4(x):
       return x

func4(1)
func4(2)
func4(3)
func4(4)

@decorator
def func5(x):
       return x

func5(1)
func5(2)
func5(3)
func5(4)
func5(5)

@decorator
def func6(x):
       return x

func6(1)
func6(2)
func6(3)

print(
    "Количество вызовов функции func1: {0} раз(а)\n"
    "Количество вызовов функции func2: {1} раз(а)\n"
    "Количество вызовов функции func3: {2} раз(а)\n"
    "Количество вызовов функции func4: {3} раз(а)\n"
    "Количество вызовов функции func5: {4} раз(а)\n"
    "Количество вызовов функции func6: {5} раз(а)".format(func1.var,func2.var,func3.var,func4.var,func5.var,func6.var)
)