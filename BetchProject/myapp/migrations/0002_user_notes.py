# Generated by Django 4.1.13 on 2024-01-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cate', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='User_Notes')),
                ('textarea', models.TextField()),
            ],
        ),
    ]
