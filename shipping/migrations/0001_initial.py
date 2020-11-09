# Generated by Django 3.1.3 on 2020-11-07 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attention_to', models.CharField(blank=True, max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(default='Austin', max_length=25)),
                ('state', models.CharField(choices=[('AL', 'Alabama - AL'), ('AK', 'Alaska - AK'), ('AZ', 'Arizona - AZ'), ('AR', 'Arkansas - AR'), ('CA', 'California - CA'), ('CO', 'Colorado - CO'), ('CT', 'Connecticut - CT'), ('DE', 'Delaware - DE'), ('FL', 'Florida - FL'), ('GA', 'Georgia - GA'), ('HI', 'Hawaii - HI'), ('ID', 'Idaho - ID'), ('IL', 'Illinois - IL'), ('IN', 'Indiana - IN'), ('IA', 'Iowa - IA'), ('KS', 'Kansas - KS'), ('KY', 'Kentucky - KY'), ('LA', 'Louisiana - LA'), ('ME', 'Maine - ME'), ('MD', 'Maryland - MD'), ('MA', 'Massachusetts - MA'), ('MI', 'Michigan - MI'), ('MN', 'Minnesota - MN'), ('MS', 'Mississippi - MS'), ('MO', 'Missouri - MO'), ('MT', 'Montana - MT'), ('NE', 'Nebraska - NE'), ('NV', 'Nevada - NV'), ('NH', 'New Hampshire - NH'), ('NJ', 'New Jersey - NJ'), ('NM', 'New Mexico - NM'), ('NY', 'New York - NY'), ('NC', 'North Carolina - NC'), ('ND', 'North Dakota - ND'), ('OH', 'Ohio - OH'), ('OK', 'Oklahoma - OK'), ('OR', 'Oregon - OR'), ('PA', 'Pennsylvania - PA'), ('RI', 'Rhode Island - RI'), ('SC', 'South Carolina - SC'), ('SD', 'South Dakota - SD'), ('TN', 'Tennessee - TN'), ('TX', 'Texas - TX'), ('UT', 'Utah - UT'), ('VT', 'Vermont - VT'), ('VA', 'Virginia - VA'), ('WA', 'Washington - WA'), ('WV', 'West Virginia - WV'), ('WI', 'Wisconsin - WI'), ('WY', 'Wyoming - WY'), ('AS', 'American Samoa - AS'), ('DC', 'District of Columbia - DC'), ('FM', 'Federated States of Micronesia - FM'), ('GU', 'Guam - GU'), ('MH', 'Marshall Islands = MH'), ('MP', 'Northern Mariana Islands - MP'), ('PW', 'Palau - PW'), ('PR', 'Puerto Rico - PR'), ('VI', 'US Virgin Islands - VI'), ('AB', 'Alberta - AB'), ('BC', 'British Columbia - BC'), ('MB', 'Manitoba - MB'), ('NB', 'New Brunswick - NB'), ('NL', 'Newfoundland - NL'), ('NS', 'Nova Scotia - NS'), ('NT', 'Northwest Territories - NT'), ('NU', 'Nunavut - NU'), ('ON', 'Ontario - ON'), ('PE', 'Prince Edward Island - PE'), ('QC', 'Quebec - QC'), ('SK', 'Saskatchewan - SK'), ('YT', 'Yukon - YT')], default='TX', max_length=2)),
                ('postal_code', models.CharField(blank=True, default='78758', max_length=10, null=True)),
                ('saved_name', models.CharField(blank=True, max_length=30, null=True)),
                ('saved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_chemicals', models.BooleanField(default=False)),
                ('has_batteries', models.BooleanField(default=False)),
                ('is_magnetized', models.BooleanField(default=False)),
                ('instruction_number', models.CharField(max_length=15, unique=True)),
                ('originating_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='originating_addresses', to='shipping.address')),
                ('ship_to_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ship_to_addresses', to='shipping.address')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(max_length=10, unique=True)),
                ('type', models.CharField(choices=[('BO', 'Box'), ('CS', 'Case'), ('CR', 'Crate'), ('DR', 'Drum'), ('PL', 'Pallet')], default='BO', max_length=2)),
                ('length', models.IntegerField(default=12)),
                ('width', models.IntegerField(default=12)),
                ('weight', models.IntegerField(default=12)),
                ('part_number', models.CharField(blank=True, max_length=7, null=True)),
                ('description', models.CharField(max_length=100)),
                ('machine_type', models.CharField(blank=True, max_length=5, null=True)),
                ('model_number', models.CharField(blank=True, max_length=5, null=True)),
                ('machine_serial', models.CharField(blank=True, max_length=25, null=True)),
                ('tracking_number', models.CharField(max_length=25, unique=True)),
                ('carrier', models.CharField(default='UPS', max_length=50)),
                ('shipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.shipment')),
            ],
        ),
    ]