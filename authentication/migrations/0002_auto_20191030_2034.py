# Generated by Django 2.2.6 on 2019-10-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Teacher'), (2, 'Student')], null=True),
        ),
    ]
