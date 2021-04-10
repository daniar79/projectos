# Generated by Django 3.1.7 on 2021-04-04 19:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_auto_20210404_1331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published'], 'verbose_name': 'Artículo', 'verbose_name_plural': 'Artículos'},
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación'),
        ),
    ]
