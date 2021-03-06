# Generated by Django 4.0.4 on 2022-06-04 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_post', models.TextField(max_length=50)),
                ('date_post', models.DateTimeField()),
                ('text_post', models.TextField(max_length=300)),
                ('image_post', models.ImageField(upload_to='post_images/')),
            ],
        ),
    ]
