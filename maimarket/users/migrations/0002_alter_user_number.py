# Generated by Django 5.1.7 on 2025-04-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.IntegerField(blank=True, max_length=12, null=True, verbose_name='Контактный телефон'),
        ),
    ]
