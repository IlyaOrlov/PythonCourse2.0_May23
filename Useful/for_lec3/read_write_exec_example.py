read = True
write = False
exec = False

print(f"Право на чтение и запись: {read == True} {write == True}")

x = 0b100
print(f"Право на чтение и запись: {x & 0b100} {write & 0b010}")
