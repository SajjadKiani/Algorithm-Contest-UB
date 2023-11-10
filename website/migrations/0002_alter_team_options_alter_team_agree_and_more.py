# Generated by Django 4.1.8 on 2023-11-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-created_date', 'team_name', 'university', 'language'], 'verbose_name': 'تیم', 'verbose_name_plural': 'تیم ها'},
        ),
        migrations.AlterField(
            model_name='team',
            name='agree',
            field=models.BooleanField(default=False, verbose_name='موافقت نامه'),
        ),
        migrations.AlterField(
            model_name='team',
            name='language',
            field=models.CharField(max_length=120, verbose_name='زبان برنامه نویسیس'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=255, verbose_name='نام تیم'),
        ),
        migrations.AlterField(
            model_name='team',
            name='university',
            field=models.CharField(max_length=255, verbose_name='نام دانشگاه'),
        ),
    ]
