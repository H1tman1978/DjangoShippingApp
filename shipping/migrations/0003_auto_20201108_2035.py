# Generated by Django 3.1.3 on 2020-11-09 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_auto_20201107_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_type', models.CharField(blank=True, max_length=5, null=True)),
                ('model', models.CharField(max_length=15)),
                ('serial_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.CharField(max_length=15)),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='package',
            name='description',
        ),
        migrations.RemoveField(
            model_name='package',
            name='part_number',
        ),
        migrations.AddField(
            model_name='package',
            name='height',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='package',
            name='weight',
            field=models.IntegerField(default=10),
        ),
    ]
