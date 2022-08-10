# Generated by Django 4.0.6 on 2022-08-08 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrofacil', '0003_remove_compras_produto_remove_produto_estoque_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='quantidade',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estoque',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
