# Generated by Django 5.2.4 on 2025-07-23 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factures', '0003_client_facture_payee'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='factures.client'),
            preserve_default=False,
        ),
    ]
