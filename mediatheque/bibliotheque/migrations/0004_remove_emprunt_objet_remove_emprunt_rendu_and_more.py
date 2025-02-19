# Generated by Django 5.1.5 on 2025-02-02 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0003_remove_emprunt_date_retour_remove_emprunt_livre_and_more'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprunt',
            name='objet',
        ),
        migrations.RemoveField(
            model_name='emprunt',
            name='rendu',
        ),
        migrations.AddField(
            model_name='emprunt',
            name='objet_id',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='emprunt',
            name='objet_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
