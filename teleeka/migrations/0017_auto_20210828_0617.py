# Generated by Django 3.1.7 on 2021-08-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleeka', '0016_client_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='note',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
