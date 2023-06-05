d = {"собака": "dog", "кошка": "cat", "table": "стол"}
# print(d["кот"])
# print(d.get("собака", "нету"))

for k, v in d.items():
    print(f"{k=}, {v=}")

d["птица"] = "bird"
d["abc"] = [1, 2, 3]

for k, v in d.items():
    print(f"{k=}, {v=}")