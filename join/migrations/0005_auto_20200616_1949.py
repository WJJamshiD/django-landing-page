# Generated by Django 3.0.6 on 2020-06-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0004_subcriber_ref_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcriber',
            name='ref_id',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
