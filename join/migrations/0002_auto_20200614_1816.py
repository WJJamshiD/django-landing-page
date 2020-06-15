# Generated by Django 3.0.6 on 2020-06-14 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='join',
            old_name='full_name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='join',
            name='first_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='join',
            name='zip_code',
            field=models.IntegerField(default=1212),
            preserve_default=False,
        ),
    ]