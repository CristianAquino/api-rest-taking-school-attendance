# Generated by Django 5.0.2 on 2024-03-03 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_attendance_justification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='missed',
            field=models.BooleanField(default=True),
        ),
    ]