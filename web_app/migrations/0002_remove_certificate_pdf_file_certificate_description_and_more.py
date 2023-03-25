# Generated by Django 4.1.7 on 2023-03-24 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='pdf_file',
        ),
        migrations.AddField(
            model_name='certificate',
            name='description',
            field=models.TextField(default='No description provided.'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='image',
            field=models.ImageField(upload_to='certificates'),
        ),
    ]