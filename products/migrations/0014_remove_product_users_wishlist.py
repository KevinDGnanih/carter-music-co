# Generated by Django 3.2 on 2023-03-25 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_product_users_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='users_wishlist',
        ),
    ]
