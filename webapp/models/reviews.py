from django.db import models
from django.db.models import TextChoices
from django.contrib.auth.models import User

from webapp.models import Product


class ModerateChoice(TextChoices):
    MODERATE = 'Moderate', 'Модерировано'
    NOMODERATE = 'No_moderate', 'Немодерировано'


class Review(models.Model):
    moderation = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        choices=ModerateChoice.choices,
        default=ModerateChoice.NOMODERATE,
        verbose_name="Модерация"
    )

    author = models.ForeignKey(
        max_length=200,
        null=False,
        blank=False,
        to=User,
        related_name='reviews',
        verbose_name='Автор',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        max_length=200,
        null=False,
        blank=False,
        to=Product,
        related_name='reviews',
        verbose_name='Товары',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
        verbose_name='Текст отзыва'
    )
    grade = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='Оценка',
        default=0
    )
    grade_stars = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name='Оценка звездочками',
        default=''
    )