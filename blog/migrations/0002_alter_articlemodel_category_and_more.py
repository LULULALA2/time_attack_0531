# Generated by Django 4.0.4 on 2022-05-31 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categorymodel'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category',
            field=models.CharField(max_length=256),
        ),
    ]
