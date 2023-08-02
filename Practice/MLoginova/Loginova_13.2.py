import mongoengine as me


class RegistryUL(me.Document):
    inn = me.StringField(max_length=10, required=True)
    name_organ = me.StringField(max_length=256, required=True)
    type_ownership = me.StringField(max_length=50)
    name_owner = me.StringField(max_length=256)
    address = me.StringField(max_length=256)

    def __repr__(self):
        return ("<RegistryUL(inn='{}'), "
                "name_organ='{}', "
                "type_ownership='{}',"
                "name_owner='{}',"
                " address='{}')>".format(self.inn,
                                         self.name_organ,
                                         self.type_ownership,
                                         self.name_owner,
                                         self.address))


if __name__ == "__main__":
    conn = me.connect('test')
    #   print(conn)
   #   Создаем документ1
    org1 = RegistryUL(inn='1234567890',
                      name_organ='SUN',
                      type_ownership='ООО',
                      name_owner='Иванов И.И.',
                      address='Россия, г.Нижний Новгород, ул. Горького, д.65')
    org1.save()
    #   Создаем документ2
    org2 = RegistryUL(inn='1234567891',
                      name_organ='Оазис',
                      type_ownership='ОАО',
                      name_owner='Петров И.И.',
                      address='Россия, г.Нижний Новгород, ул. Ильниская, д.45')
    org2.save()
    #   Создаем документ3
    org3 = RegistryUL(inn='1234567892',
                      name_organ='Генезис',
                      type_ownership='ПАО',
                      name_owner='Сидоров И.И.',
                      address='Россия, г.Нижний Новгород, ул. Обухова, д.20')
    org3.save()
    print(f"Документов в базе:{RegistryUL.objects.count()}")
    input_inn = ' '
    while len(input_inn := input("Введите ИНН ЮЛ(10 символов): ")) != 10:
        print(f'Вы ввели ИНН из {len(input_inn)} символов, нужно из 10. Повторите ввод!')
    print(f"Информация по ЮЛ по ИНН {input_inn}:\n {RegistryUL.objects.filter(inn=input_inn)}")
    RegistryUL.objects.delete()
