# Generated by Django 4.2.5 on 2023-09-23 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_alter_member_options_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(default='c:/Users/err_r/Pictures/th.jpg', upload_to='images/'),
        ),
    ]