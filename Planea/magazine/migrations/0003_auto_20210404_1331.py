# Generated by Django 3.1.7 on 2021-04-04 11:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_article_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 4, 11, 31, 9, 757464, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='articles', verbose_name='Imagen'),
        ),
    ]