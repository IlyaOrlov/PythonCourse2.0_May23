from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Film(models.Model):
    #атрибуты name, desc, pub_date, rate  - столбцы
    name = models.CharField(max_length=200)
    # TextField() - тип поля
    state = models.TextField(null=True)
    date_exist = models.DateField(default='0')
    desc = models.TextField()
    # 'date published' - как поле будет выглядеть при выводе на экран в терминале
    # auto_now_add=True - когда будет добавляться новая запись,
    # это поле будет автоматически проставляться, исходя из текущего времени
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=1)


class Comments(models.Model):
    films_id = models.ForeignKey(Film, on_delete=models.CASCADE, null=True)
    comment = models.TextField()



