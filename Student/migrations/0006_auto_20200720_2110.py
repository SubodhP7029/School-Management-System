# Generated by Django 3.0.3 on 2020-07-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_auto_20200720_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]),
        ),
    ]
