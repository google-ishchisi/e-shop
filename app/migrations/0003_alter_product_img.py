# Generated by Django 4.0.5 on 2022-08-25 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='img/no-foto.jpg', upload_to='img/'),
        ),
    ]
