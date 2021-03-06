# Generated by Django 4.0.1 on 2022-01-29 16:53

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
                ('title', models.CharField(db_index=True, max_length=250, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('text', models.TextField(verbose_name='Text')),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ('-published',),
            },
        ),
    ]
