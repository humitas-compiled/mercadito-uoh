# Generated by Django 5.2.4 on 2025-07-13 20:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vender', '0004_alter_producto_categoria'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_comprados', to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vender.producto')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_vendidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('enviado_en', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='chat.chat')),
            ],
        ),
    ]
