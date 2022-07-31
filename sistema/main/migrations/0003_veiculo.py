# Generated by Django 4.0.6 on 2022-07-31 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_empresa_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('renavam', models.CharField(max_length=9)),
                ('chassi', models.CharField(max_length=17)),
                ('antt', models.CharField(max_length=11)),
                ('disponibilidade', models.IntegerField(choices=[(1, 'Ativo'), (2, 'Vendido')], default=1)),
                ('pesoCubagem', models.PositiveIntegerField(blank=True, null=True)),
                ('pesoTotal', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
