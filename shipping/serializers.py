from rest_framework import serializers
from .models import Shipment, Package, Part, Machine


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'originating_address',
            'ship_to_address',
            'has_chemicals',
            'has_batteries',
            'is_magnetized',
            'instruction_number',
            'has_shipped',
        )
        model = Shipment


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'case_number',
            'type',
            'length',
            'width',
            'height',
            'weight',
            'tracking_number',
            'carrier',
            'shipment_id',
            'date_shipped',
        )
        model = Package


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'part_number',
            'quantity',
            'description',
            'package_id',
        )
        model = Part


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'machine_type',
            'model',
            'serial_number',
            'description',
            'package_id',
        )
        model = Machine
