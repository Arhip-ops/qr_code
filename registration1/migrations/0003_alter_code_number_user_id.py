# Generated by Django 5.1.3 on 2025-01-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration1', '0002_code_number_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code_number',
            name='user_id',
            field=models.SmallIntegerField(max_length=6),
        ),
    ]
