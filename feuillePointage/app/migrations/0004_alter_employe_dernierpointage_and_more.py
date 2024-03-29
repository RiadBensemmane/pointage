# Generated by Django 5.0.2 on 2024-02-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_employe_datedernierpointage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='dernierPointage',
            field=models.CharField(choices=[('I', 'I'), ('7', '7'), ('R', 'R'), ('Cr', 'Cr'), ('T', 'T'), ('1', '1'), ('C', 'C'), ('6', '6'), ('A', 'A'), ('M', 'M'), ('8', '8'), ('2', '2'), ('9', '9')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='situationFamiliale',
            field=models.CharField(choices=[('divorcé', 'divorcé(e)'), ('célibataire', 'célibataire'), ('veuf', 'veuf(ve)'), ('marié', 'marié(e)')], max_length=100, null=True),
        ),
    ]
