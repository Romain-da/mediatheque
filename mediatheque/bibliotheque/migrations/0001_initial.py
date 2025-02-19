# Generated by Django 5.1.5 on 2025-01-30 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JeuDePlateau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('createur', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bloque', models.BooleanField(default=False)),
                ('emprunts_actifs', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_emprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('titre', models.CharField(max_length=255)),
                ('auteur', models.CharField(max_length=255)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliotheque.membre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_emprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('realisateur', models.CharField(max_length=255)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliotheque.membre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_emprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('artiste', models.CharField(max_length=255)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliotheque.membre')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
