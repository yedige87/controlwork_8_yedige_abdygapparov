from django.db import models
from django.db.models import TextChoices


class CategoryChoice(TextChoices):
    OTHER = 'Other', 'Разное'
    TELEPHONE = 'Phone', 'Телефоны'
    LAPTOP = 'Laptop', 'Ноутбуки'
    TV = 'TV', 'Телевизоры'


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Наименование товара"
    )
    category = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        choices=CategoryChoice.choices,
        default=CategoryChoice.OTHER,
        verbose_name="Категория товара"
    )
    text = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Описание товара"
    )
    photo = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Изображение продукта',
        default='blank.jpg'
    )

    average_grade = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='Средняя Оценка',
        default=0
    )
    average_grade_stars = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name='Средняя оценка звездочками',
        default=''
    )