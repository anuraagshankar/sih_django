# Generated by Django 2.2 on 2020-01-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200109_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='N/A', max_length=100)),
                ('photo', models.ImageField(default='/home/anuraag/sih/sih/photos/default.jpg', upload_to='')),
            ],
        ),
    ]