# Generated by Django 4.1.1 on 2022-09-15 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(to='web.tag'),
        ),
    ]
