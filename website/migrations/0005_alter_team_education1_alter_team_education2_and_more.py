# Generated by Django 4.1.8 on 2023-11-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_team_major1_team_major2_team_major3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='education1',
            field=models.CharField(blank=True, choices=[('1', 'دانش آموز'), ('2', 'دانشجو'), ('3', 'دانش آموخته'), ('4', 'هیچکدام')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='education2',
            field=models.CharField(blank=True, choices=[('1', 'دانش آموز'), ('2', 'دانشجو'), ('3', 'دانش آموخته'), ('4', 'هیچکدام')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='education3',
            field=models.CharField(blank=True, choices=[('1', 'دانش آموز'), ('2', 'دانشجو'), ('3', 'دانش آموخته'), ('4', 'هیچکدام')], max_length=1, null=True),
        ),
    ]
