from utils.decorators import json_response
from novaposhta.models import NovaOffice, NovaCity


@json_response
def index(request):
    return NovaOffice.objects.all()


@json_response
def city(request):
    q = request.GET.get('q', None)

    if q is None:
        return NovaCity.objects.all()
    else:
        return sorted(NovaCity.objects.filter(name__icontains=q).all(), key=lambda t: t.name.lower().find(q.lower()))


@json_response
def office(request, city_id=None):
    from django.db.models import Q

    q = request.GET.get('q', None)

    queryset = NovaOffice.objects.filter(city_id=city_id)

    if q is not None:
        queryset = queryset.filter(Q(address__icontains=q) | Q(name__icontains=q))

    return queryset
