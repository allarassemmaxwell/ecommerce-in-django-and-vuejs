# Generated by Django 3.2.5 on 2021-08-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
