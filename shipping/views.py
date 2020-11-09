from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from .models import Shipment, Package


# Create your views here.
def index(request):
    latest_shipments_list = Shipment.objects.order_by('-instruction_number')[:5]
    context = {'latest_shipments_list': latest_shipments_list}
    return render(request, 'shipping/index.html', context)


def detail(request, shipment_id):
    shipment = get_object_or_404(Shipment, pk=shipment_id)
    package_list = get_list_or_404(Package, shipment_id=shipment.id)
    return render(request, 'shipping/details.html', {'shipment': shipment, 'packages': package_list})
