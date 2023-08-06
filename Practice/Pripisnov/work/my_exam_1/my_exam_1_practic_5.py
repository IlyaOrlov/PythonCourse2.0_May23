def count_symbol(string, symbol):


    count = 0
    for char in string:
        if char == symbol:
            count += 1
    return count


result = count_symbol("Hi, Elvis, I am here!", "i")
print(result)
