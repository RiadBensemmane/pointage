# Generated by Django 4.2.3 on 2024-02-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('matricule', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=200)),
                ('fonction', models.CharField(max_length=100)),
                ('dateRecrutement', models.DateField()),
                ('dateDetachement', models.DateField(null=True)),
                ('affectOrigine', models.CharField(max_length=100)),
                ('situationFamiliale', models.CharField(choices=[('veuf', 'veuf(ve)'), ('divorcé', 'divorcé(e)'), ('marié', 'marié(e)'), ('célibataire', 'célibataire')], max_length=100)),
                ('nbrEnfants', models.PositiveIntegerField()),
                ('dernierPointage', models.CharField(choices=[('1', '1'), ('I', 'I'), ('A', 'A'), ('7', '7'), ('6', '6'), ('M', 'M'), ('R', 'R'), ('T', 'T'), ('C', 'C'), ('Cr', 'Cr'), ('9', '9'), ('2', '2'), ('8', '8')], default=None, max_length=2, null=True)),
            ],
        ),
    ]