import pickle
from worker import Worker


john = Worker()
john.set_name('John')
john.set_age(25)
john.set_salary(1000)
jack = Worker()
jack.set_name('Jack')
jack.set_age(26)
jack.set_salary(2000)

workers = []

with open("dumpfile", "wb") as f:
    pickle.dump(Worker, f, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(workers, f, protocol=pickle.HIGHEST_PROTOCOL)

print(pickle.dumps(Worker))