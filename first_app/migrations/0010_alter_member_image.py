# Generated by Django 4.2.5 on 2023-09-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_alter_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='images/th.jpg', upload_to='images/'),
        ),
    ]
