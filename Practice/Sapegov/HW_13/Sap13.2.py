import mongoengine as me


class UL(me.Document):
    inn = me.StringField(required=True, max_length=10, min_length=10, unique=True)
    name_ul = me.StringField(max_length=50)
    form_s = me.StringField(max_length=50)
    fio = me.StringField(max_length=50)
    address = me.StringField(max_length=50)

    def __repr__(self):
        return f'UL(inn: {self.inn}, name_ul: {self.name_ul}, '\
               f'form_s: {self.form_s}, fio: {self.fio}, address: {self.address}'


if __name__ == "__main__":
    with (me.connect('test')) as conn:
        UL(inn='1111111111',
           name_ul='Sber',
           form_s='OOO',
           fio='Ivanov I.I.',
           address='Moscow').save()

        UL(inn='2222222222',
           name_ul='VTB',
           form_s='PAO',
           fio='Petrov P.P.',
           address='Ekb').save()

        UL(inn='3333333333',
           name_ul='GAZ',
           form_s='IP',
           fio='Sidorov S.S.',
           address='N.Novgorod').save()

        inn = input('Введите ИНН требуемой организации: ')
        print(UL.objects.filter(inn=inn))

        UL.objects.delete()
