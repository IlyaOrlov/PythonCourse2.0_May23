
def decorate(func):
    def inner():
        print("========")
        func()
        print("========")
    return inner()


@decorate
def prosto():
    print("Hi")
