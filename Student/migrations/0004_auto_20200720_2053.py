# Generated by Django 3.0.3 on 2020-07-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_auto_20200720_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
