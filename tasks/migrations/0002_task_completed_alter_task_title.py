# Generated by Django 5.1.1 on 2024-09-10 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="task",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Título"),
        ),
    ]
