# Generated by Django 4.1.6 on 2023-03-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='text',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Описание товара'),
        ),
    ]
