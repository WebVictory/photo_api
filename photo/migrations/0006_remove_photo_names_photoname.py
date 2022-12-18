# Generated by Django 4.1.4 on 2022-12-17 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_alter_photo_created_at_alter_photo_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='names',
        ),
        migrations.CreateModel(
            name='PhotoName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_name', to='photo.photo')),
            ],
        ),
    ]