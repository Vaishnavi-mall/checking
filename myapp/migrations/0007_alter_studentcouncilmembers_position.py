# Generated by Django 4.0.2 on 2022-04-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_studentcouncilmembers_is_design_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcouncilmembers',
            name='position',
            field=models.CharField(choices=[('P', 'President'), ('R', 'Vice President'), ('S', 'Secretary'), ('T', 'Treasurer'), ('JS', 'Joint Secretary'), ('JT', 'Joint Treasurer'), ('C', 'Coordinator')], max_length=50),
        ),
    ]
