# Generated by Django 3.2.7 on 2021-09-14 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoEcommerceApp', '0003_productabout_productdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_bannners1', models.ImageField(upload_to='media')),
                ('top_bannners2', models.ImageField(upload_to='media')),
                ('top_bannners3', models.ImageField(upload_to='media')),
                ('ad_banner', models.ImageField(upload_to='media')),
                ('banner_left', models.ImageField(upload_to='media')),
                ('banner_right', models.ImageField(upload_to='media')),
            ],
        ),
    ]
