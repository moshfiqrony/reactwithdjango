# Generated by Django 2.1.5 on 2019-01-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='NEW', max_length=100),
            preserve_default=False,
        ),
    ]