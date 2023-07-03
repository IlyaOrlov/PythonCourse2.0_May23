class Action:
    def doaction(self):
        print("I'm moving")


class Fly(Action):
    def doaction(self):
        print("I'm flying")


class Swim(Action):
    def doaction(self):
        print("I'm swimming")


class Hero:
    def __init__(self):
        self._action = Action()

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        if isinstance(action, Action):
            self._action = action


h = Hero()
i = input("Введите 1-fly или 2-swim: ")
if i == "1":
    h.action = Fly()
elif i == "2":
    h.action = Swim()
else:
    h.action = "123"
h.action.doaction()
