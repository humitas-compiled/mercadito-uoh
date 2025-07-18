# Generated by Django 5.2.4 on 2025-07-14 02:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(choices=[('producto', 'Producto'), ('chat', 'Chat')], max_length=10)),
                ('usuario_comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportes_realizados', to=settings.AUTH_USER_MODEL)),
                ('usuario_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportes_recibidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
