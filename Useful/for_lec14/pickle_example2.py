import pickle


with open("dumpfile", "rb") as f:
    Worker = pickle.load(f)
    workers = pickle.load(f)

print(f"j1={next(iter(workers), 'No workers')}")

