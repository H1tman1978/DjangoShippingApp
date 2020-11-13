from django.forms import ModelForm, Form, BooleanField
from .models import Address, Shipment, Package, Part, Machine


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['created_by']


class HasChemicalsForm(Form):
    chemicals_yes = BooleanField(required=False)
    chemicals_no = BooleanField(required=False)
    chemicals_no.label = 'No'
    chemicals_yes.label = 'Yes'


class HasBatteriesForm(Form):
    has_batteries_no = BooleanField(required=False)
    has_batteries_yes = BooleanField(required=False)
    has_batteries_yes.label = 'Yes'
    has_batteries_no.label = 'No'


class IsMagnetizedForm(Form):
    is_magnetized = BooleanField(required=False)


class PackageForm(ModelForm):
    class Meta:
        model = Package
        exclude = ['date_shipped', 'shipment_id']


class PartForm(ModelForm):
    class Meta:
        model = Part
        exclude = ['package_id']


class MachineForm(ModelForm):
    class Meta:
        model = Machine
        exclude = ['package_id']
