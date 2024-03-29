# Generated by Django 2.2.3 on 2019-07-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.CharField(max_length=200)),
                ('product_price', models.IntegerField(default=0)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('remain_product', models.IntegerField(default=0)),
            ],
        ),
    ]
