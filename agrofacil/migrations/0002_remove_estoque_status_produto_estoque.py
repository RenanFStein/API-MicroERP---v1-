# Generated by Django 4.0.6 on 2022-08-08 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agrofacil', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoque',
            name='status',
        ),
        migrations.AddField(
            model_name='produto',
            name='estoque',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agrofacil.estoque', verbose_name='Estoque'),
            preserve_default=False,
        ),
    ]
