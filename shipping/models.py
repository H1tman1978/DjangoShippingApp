from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Address(models.Model):
    STATE_PROVINCE_CHOICES = [
        # US States
        ('AL', 'Alabama - AL'),
        ('AK', 'Alaska - AK'),
        ('AZ', 'Arizona - AZ'),
        ('AR', 'Arkansas - AR'),
        ('CA', 'California - CA'),
        ('CO', 'Colorado - CO'),
        ('CT', 'Connecticut - CT'),
        ('DE', 'Delaware - DE'),
        ('FL', 'Florida - FL'),
        ('GA', 'Georgia - GA'),
        ('HI', 'Hawaii - HI'),
        ('ID', 'Idaho - ID'),
        ('IL', 'Illinois - IL'),
        ('IN', 'Indiana - IN'),
        ('IA', 'Iowa - IA'),
        ('KS', 'Kansas - KS'),
        ('KY', 'Kentucky - KY'),
        ('LA', 'Louisiana - LA'),
        ('ME', 'Maine - ME'),
        ('MD', 'Maryland - MD'),
        ('MA', 'Massachusetts - MA'),
        ('MI', 'Michigan - MI'),
        ('MN', 'Minnesota - MN'),
        ('MS', 'Mississippi - MS'),
        ('MO', 'Missouri - MO'),
        ('MT', 'Montana - MT'),
        ('NE', 'Nebraska - NE'),
        ('NV', 'Nevada - NV'),
        ('NH', 'New Hampshire - NH'),
        ('NJ', 'New Jersey - NJ'),
        ('NM', 'New Mexico - NM'),
        ('NY', 'New York - NY'),
        ('NC', 'North Carolina - NC'),
        ('ND', 'North Dakota - ND'),
        ('OH', 'Ohio - OH'),
        ('OK', 'Oklahoma - OK'),
        ('OR', 'Oregon - OR'),
        ('PA', 'Pennsylvania - PA'),
        ('RI', 'Rhode Island - RI'),
        ('SC', 'South Carolina - SC'),
        ('SD', 'South Dakota - SD'),
        ('TN', 'Tennessee - TN'),
        ('TX', 'Texas - TX'),
        ('UT', 'Utah - UT'),
        ('VT', 'Vermont - VT'),
        ('VA', 'Virginia - VA'),
        ('WA', 'Washington - WA'),
        ('WV', 'West Virginia - WV'),
        ('WI', 'Wisconsin - WI'),
        ('WY', 'Wyoming - WY'),
        # US Commonwealth and Territories
        ('AS', 'American Samoa - AS'),
        ('DC', 'District of Columbia - DC'),
        ('FM', 'Federated States of Micronesia - FM'),
        ('GU', 'Guam - GU'),
        ('MH', 'Marshall Islands = MH'),
        ('MP', 'Northern Mariana Islands - MP'),
        ('PW', 'Palau - PW'),
        ('PR', 'Puerto Rico - PR'),
        ('VI', 'US Virgin Islands - VI'),
        # Canadian Provinces and Territories
        ('AB', 'Alberta - AB'),
        ('BC', 'British Columbia - BC'),
        ('MB', 'Manitoba - MB'),
        ('NB', 'New Brunswick - NB'),
        ('NL', 'Newfoundland - NL'),
        ('NS', 'Nova Scotia - NS'),
        ('NT', 'Northwest Territories - NT'),
        ('NU', 'Nunavut - NU'),
        ('ON', 'Ontario - ON'),
        ('PE', 'Prince Edward Island - PE'),
        ('QC', 'Quebec - QC'),
        ('SK', 'Saskatchewan - SK'),
        ('YT', 'Yukon - YT'),
    ]
    attention_to = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    address1 = models.CharField(max_length=50, blank=False)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=25, blank=False, default="Austin")
    state = models.CharField(max_length=2, choices=STATE_PROVINCE_CHOICES, default="TX", blank=False)
    postal_code = models.CharField(max_length=10, default="78758", blank=True, null=True)
    saved_name = models.CharField(max_length=30, blank=True, null=True)
    saved_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.saved_name}"


class Shipment(models.Model):
    originating_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='originating_addresses')
    ship_to_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='ship_to_addresses')
    has_chemicals = models.BooleanField(default=False)
    has_batteries = models.BooleanField(default=False)
    is_magnetized = models.BooleanField(default=False)
    instruction_number = models.CharField(max_length=15, unique=True)  # Refers to Shipment Instruction Number
    has_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.instruction_number}"


class Package(models.Model):
    UNIT_TYPES = [
        ('BO', 'Box'),
        ('CS', 'Case'),
        ('CR', 'Crate'),
        ('DR', 'Drum'),
        ('PL', 'Pallet'),
    ]

    case_number = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=2, choices=UNIT_TYPES, default='BO')
    length = models.IntegerField(blank=False, default=12)
    width = models.IntegerField(blank=False, default=12)
    height = models.IntegerField(blank=False, default=12)
    weight = models.IntegerField(blank=False, default=10)
    tracking_number = models.CharField(max_length=25, unique=True)
    carrier = models.CharField(max_length=50, default='UPS')
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    date_shipped = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f"{self.case_number}"


class Part(models.Model):
    """Model for Parts"""
    part_number = models.CharField(max_length=15, blank=False)
    quantity = models.IntegerField(blank=False)
    description = models.CharField(max_length=50, blank=False)
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.part_number}"


class Machine(models.Model):
    machine_type = models.CharField(max_length=5, blank=True, null=True)
    model = models.CharField(max_length=15, blank=False)
    serial_number = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=50, blank=False)
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.machine_type}-{self.model}: {self.serial_number}"
