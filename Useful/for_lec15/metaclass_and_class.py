# class MyMeta(type):
#     pass


class Employee:
    pass

# class Manager(Employee):
#     pass

Manager = type('Manager', (Employee,), {'name': 'Petr'})
#
# m = Manager()
# print(m.name)



MyMeta = type('MyMeta', (type,), {})

MyClass = MyMeta('MyClass', tuple(), {'attr': 250})

obj = MyClass()
print(obj.attr)

