def my_decorator(func):
    def wrap_func():
        print("***********")
        func()
        print("******************")
    return wrap_func


def hello():
    print("hellloooooooooo")


def bye():
    print("see you later")

a = my_decorator(hello)
a()

