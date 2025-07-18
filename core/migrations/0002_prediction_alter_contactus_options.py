# Generated by Django 5.1.5 on 2025-02-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
            ],
            options={
                'verbose_name': 'Prediction',
                'verbose_name_plural': 'Predictions',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Contact Us', 'verbose_name_plural': 'Contact Us'},
        ),
    ]
