# Generated by Django 2.2.3 on 2019-07-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_shoppingcar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, default='photos/TV.jpg', null=True, upload_to='photos/'),
        ),
    ]
