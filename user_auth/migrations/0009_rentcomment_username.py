# Generated by Django 4.1.3 on 2023-05-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0008_alter_poster_poster_image_one_rentcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentcomment',
            name='username',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
