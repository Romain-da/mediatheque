# Generated by Django 5.1.5 on 2025-02-01 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateField(auto_now_add=True)),
                ('date_retour', models.DateField(blank=True, null=True)),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.livre')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprunts', to='bibliotheque.membre')),
            ],
        ),
    ]
