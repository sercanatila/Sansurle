# Generated by Django 3.2.2 on 2021-05-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TranscribeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.CharField(blank=True, max_length=100, null=True)),
                ('video', models.FileField(upload_to='sample_inputs')),
            ],
        ),
    ]