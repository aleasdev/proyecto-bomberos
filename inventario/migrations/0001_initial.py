# Generated by Django 4.2.4 on 2023-11-03 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabina',
            fields=[
                ('id_cabina', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cabina', models.CharField(max_length=15)),
                ('item', models.IntegerField()),
                ('elemento', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30, null=True)),
                ('observaciones', models.CharField(max_length=100, null=True)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCarro',
            fields=[
                ('id_tp_carro', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_carro', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id_carro', models.AutoField(primary_key=True, serialize=False)),
                ('id_cabina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.cabina')),
                ('id_tp_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.tipocarro')),
            ],
        ),
        migrations.AddField(
            model_name='cabina',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.estado'),
        ),
    ]