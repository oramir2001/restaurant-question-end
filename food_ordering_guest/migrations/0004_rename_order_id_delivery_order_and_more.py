# Generated by Django 4.1.7 on 2023-04-19 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_ordering_guest', '0003_rename_user_id_cart_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='cart_id',
            new_name='cart',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='dish_id',
            new_name='dish',
        ),
    ]
