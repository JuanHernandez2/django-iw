# Generated by Django 2.2.3 on 2019-07-15 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('state', models.CharField(choices=[('A', 'Active'), ('U', 'Unactive')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='MunicipalityXRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='municipalities.Municipality')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('municipalities', models.ManyToManyField(through='municipalities.MunicipalityXRegion', to='municipalities.Municipality')),
            ],
        ),
        migrations.AddField(
            model_name='municipalityxregion',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='municipalities.Region'),
        ),
    ]
