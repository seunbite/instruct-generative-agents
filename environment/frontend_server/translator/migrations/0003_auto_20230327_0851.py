# Generated by Django 2.2 on 2023-03-27 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0002_evaldata_target_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaldata',
            name='target_agent',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]