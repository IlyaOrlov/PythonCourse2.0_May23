class A:
    def say_hello(self):
        print("hello A")

class B:
    def say_hello(self):
        print("hello B")

class D:
    def say_hello(self):
        print("hello D")

class C(A, B, D):
    def say_hello(self):
        super(B, self).say_hello()


c = C()
c.say_hello()