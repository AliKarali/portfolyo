# Generated by Django 5.0.4 on 2024-05-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=100, verbose_name='Project Name')),
                ('projectImage', models.FileField(blank=True, null=True, upload_to='Project Cover', verbose_name='Project Cover')),
                ('projectURL', models.TextField(max_length=1000, verbose_name='Project Link')),
            ],
        ),
    ]
