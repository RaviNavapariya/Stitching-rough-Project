# Generated by Django 4.1.1 on 2022-09-20 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(default='Owner', on_delete=django.db.models.deletion.CASCADE, to='log.userrole'),
        ),
    ]
