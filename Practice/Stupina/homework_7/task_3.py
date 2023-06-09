d = {'работать': 'в отпуск', '!': '!!!'}
message = 'Я хочу Работать!'.lower()
print(f'старая строка: {message}')

for key, val in d.items():
    message = message.replace(key, val)
print(f'новая строка: {message}')
