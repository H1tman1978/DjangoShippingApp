from rest_framework import generics

from .models import Shipment, Package, Part, Machine
from .serializers import ShipmentSerializer, PackageSerializer, PartSerializer, MachineSerializer

class ListShipment(generics.ListCreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class DetailShipment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class ListPackage(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class DetailPackage(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class ListPart(generics.ListCreateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class DetailPart(generics.RetrieveUpdateDestroyAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class ListMachine(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class DetailMachine(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
