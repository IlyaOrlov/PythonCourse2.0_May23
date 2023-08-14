# Реализовать NoSQL базу данных для хранения реестра юридических
# лиц, содержащей ИНН, название организации, форму собственности,
# ФИО владельца, адрес. Написать приложение, позволяющее искать данные в базе по ИНН.
import mongoengine as me


class UL(me.Document):
    inn = me.StringField(required=True, max_length=10, min_length=10)
    name_ul = me.StringField(max_length=50)
    form_s = me.StringField(max_length=50)
    fio = me.StringField(max_length=50)
    address = me.StringField(max_length=50)

    def __repr__(self):
        return f'UL(inn: {self.inn}, name_ul: {self.name_ul}, '\
               f'form_s: {self.form_s}, fio: {self.fio}, address: {self.address}'


conn = me.connect('test')

UL(inn='1111111111',
    name_ul='Sber',
    form_s='OOO',
    fio='Ivanov I.I.',
    address='Moscow').save()

UL(inn='2111111111',
    name_ul='Ашан',
    form_s='ПАО',
    fio='Пупкин А.И',
    address='г.Абакан').save()

UL(inn='3111111111',
    name_ul='Теле2',
    form_s='ПАО',
    fio='Богатов И.И',
    address='г.Симферопль')

UL(inn='4111111111',
    name_ul='Ростелеком',
    form_s='ЗАО',
    fio='Зотов В.В',
    address='г.Рославль')
UL(inn='5111111111',
    name_ul='КиБ',
    form_s='ООО',
    fio='Васильев С.С',
    address='г.Бирбиджан')
print('Документов в базе: {}'.format(UL.objects.count()))

# Делаем запрос
print(UL.objects.filter(inn='1111111111'))
UL.objects.delete()
conn.close()
