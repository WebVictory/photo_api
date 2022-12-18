# Generated by Django 4.1.4 on 2022-12-16 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='names',
        ),
        migrations.CreateModel(
            name='MetaName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.photo')),
            ],
        ),
    ]
