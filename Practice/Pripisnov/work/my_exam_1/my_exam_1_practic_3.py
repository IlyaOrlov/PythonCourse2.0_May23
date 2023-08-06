def custom_range(start, stop=None, step=1):


    if stop is None:
        stop = start
        start = 0


    if step == 0:
        raise ValueError("Шаг не может быть равен нулю.")

    result = []
    i = start
    while (step > 0 and i < stop) or (step < 0 and i > stop):
        result.append(i)
        i += step

    return result
print(custom_range(5))
print(custom_range(1, 6))
print(custom_range(1, 10, 2))
print(custom_range(10, 1, -2))
