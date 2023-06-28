
class Pizza:
    def make_base(self):
        print("Base ready")

    def bake(self):
        print("Baked")

    def __str__(self):
        return f"Pizza {type(self)} is ready"


class MushPizza(Pizza):
    def add_ingr(self):
        print("Added mushrooms")

class VegPizza(Pizza):
    def add_ingr(self):
        print("Added vegetables")

class MeatPizza(Pizza):
    def add_ingr(self):
        print("Added meat")


def make_pizza(pizza):
    pizza.add_ingr()
    pizza.bake()
    print(pizza)


make_pizza(MushPizza())
make_pizza(MeatPizza())
make_pizza(VegPizza())
