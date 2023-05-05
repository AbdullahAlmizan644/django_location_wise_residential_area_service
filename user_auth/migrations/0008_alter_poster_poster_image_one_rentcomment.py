# Generated by Django 4.1.3 on 2023-05-05 11:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0007_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='poster_image_one',
            field=models.ImageField(upload_to='images/', verbose_name='poseter image one size-->width:1170 height:780'),
        ),
        migrations.CreateModel(
            name='RentComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_auth.rent')),
            ],
        ),
    ]