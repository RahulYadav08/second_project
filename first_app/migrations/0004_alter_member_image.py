# Generated by Django 4.2.5 on 2023-09-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='C:/Users/err_r/Pictures/th.jpg', upload_to='images/'),
        ),
    ]
