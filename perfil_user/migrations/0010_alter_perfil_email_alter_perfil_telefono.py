# Generated by Django 5.2.4 on 2025-07-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil_user', '0009_alter_perfil_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
