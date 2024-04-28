# Generated by Django 5.0.4 on 2024-04-26 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_information',
            field=models.CharField(max_length=200, null=True, verbose_name='Контактная информация'),
        ),
        migrations.AlterField(
            model_name='user',
            name='experience',
            field=models.CharField(max_length=200, null=True, verbose_name='Опыт'),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
