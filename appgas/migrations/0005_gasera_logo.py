# Generated by Django 2.2.6 on 2019-10-14 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appgas', '0004_detallespedido_pedido_pedidosxempleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasera',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
