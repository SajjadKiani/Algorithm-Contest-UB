# Generated by Django 4.1.8 on 2023-11-12 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_team_options_alter_team_education1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='major1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='major2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='major3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='education1',
            field=models.CharField(blank=True, choices=[('1', 'دانش آموز'), ('2', 'دانشجو'), ('3', 'دانش آموخته')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='education2',
            field=models.CharField(blank=True, choices=[('1', 'دانش آموز'), ('2', 'دانشجو'), ('3', 'دانش آموخته')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='education3',
            field=models.CharField(blank=True, choices=[('1', 'دانش آموز'), ('2', 'دانشجو'), ('3', 'دانش آموخته')], max_length=1, null=True),
        ),
    ]
