# Generated by Django 2.1.5 on 2019-04-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]