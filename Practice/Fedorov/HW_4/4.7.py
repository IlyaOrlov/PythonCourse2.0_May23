
def decorate(func):
    def inner(*args, **kwargs):
        print("========")
        func(*args, **kwargs)
        print("========")
    return inner()


@decorate
def prosto():
    print("Hi")
