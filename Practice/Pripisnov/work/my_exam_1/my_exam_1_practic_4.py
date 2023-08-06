def to_title(x):


    y = x.split()
    capitalized_words = [word.capitalize() for word in y]
    return ' '.join(capitalized_words)


result = to_title('orlov Ilya evgenyevich')
print(result)
