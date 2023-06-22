class TestManager:

    def __enter__(self):
        print('Starting code inside manager')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Code completed. Error info: type - {exc_type}')


print(0)
with TestManager():
    print(1)
    z = 50
    print(2)
    #x = z / 0
    print(3)
print(4)
