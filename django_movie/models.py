from django.db import models


class Category(models.Model):
    """Категория"""
    name = models.CharField('Категория', max_length=255)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


class Actor(models.Model):
    """Актеры и режжисеры"""
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='actors/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Актеры и режжисеры'
        verbose_name_plural = 'Актеры и режжисеры'


class Genre(models.Model):
    """Жанры"""
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанр'
