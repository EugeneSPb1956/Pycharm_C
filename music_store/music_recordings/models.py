from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Artists(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название группы')
    country = models.CharField(max_length=15, default='N/A', verbose_name='Страна происхождения')
    city = models.CharField(max_length=15, default='N/A', verbose_name='Город')
    year1 = models.IntegerField(null=True, verbose_name='Год начала деятельности')
    year2 = models.IntegerField(null=True, verbose_name='Окончание')
    active = models.BooleanField(verbose_name='Продолжают работать')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Studio(models.Model):
    name = models.CharField(max_length=15, verbose_name='Студия звукозаписи')
    country = models.CharField(max_length=15, default='N/A', verbose_name='Страна')
    city = models.CharField(max_length=15, default='N/A', verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студия звукозаписи'
        verbose_name_plural = 'Студии звукозаписи'


class Albums(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название альбома')
    # artists_id = models.IntegerField()
    artists_id = models.ForeignKey(Artists, on_delete=models.CASCADE)
    # studio_id = models.IntegerField()
    studio_id = models.ForeignKey(Studio, on_delete=models.CASCADE)
    lable = models.CharField(max_length=15, default='N/A', verbose_name='Лэйбл')
    release = models.IntegerField(null=True, verbose_name='Год выпуска')
    genre = models.CharField(max_length=10, default='N/A', verbose_name='Жанр')
    price = models.DecimalField(max_digits=11, null=True, decimal_places=2, verbose_name='Цена за диск')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Tracks(models.Model):
    album_id = models.ForeignKey(Albums, on_delete=models.CASCADE)
    number = models.IntegerField(null=True, verbose_name='Номер композиции п/п')
    title = models.CharField(max_length=20, verbose_name='Название')
    writer = models.CharField(max_length=20, default='N/A', verbose_name='Композитор/Поэт')
    lyrics = models.TextField(verbose_name='Текст', default='N/A')
    length = models.DateTimeField(null=True, verbose_name='Длительность звучания')  # ?

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Композиция'
        verbose_name_plural = 'Композиции'
