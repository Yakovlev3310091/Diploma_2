# Generated by Django 4.0.1 on 2022-12-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0005_alter_goal_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]