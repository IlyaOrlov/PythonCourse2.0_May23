def byefun(f):
    f()
    print("bye")


def hellofun():
    print("hello")


byefun(hellofun)
