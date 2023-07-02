import pickle
from task_4 import Human


def fun_load(name_f):
    with open(name_f, 'rb') as f:
        man = pickle.load(f)
        for i in man:
            print(i)


fun_load('human')
