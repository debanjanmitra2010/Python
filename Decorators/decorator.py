# Higher Order Function HOC
# when calling a function


def hello(func):
    func()


def greet():
    print("I'm here")


a = hello(greet)
print(a)

# When returning a function


def greet2():
    def func():
        return 5

    return func()

# Decorator


def my_decorator(func):
    def wrap_func():
        print("*************")
        func()
        print("*************")

    return wrap_func()


@my_decorator
def hello():
    print("Helllloooooo, My Name is Debanjan")


@my_decorator
def bye():
    print("See you later")

# Decorator with many arguments


def my_decorator2(func):
    def wrap_func2(*args, **kwargs):
        func(*args, **kwargs)

    return wrap_func2


@my_decorator2
def greet3(greeting, emoji=':)'):
    print(greeting, emoji)


greet3('hiii')
