# Generated by Django 3.0.8 on 2021-01-02 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20200808_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
