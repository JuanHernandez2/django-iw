from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Region, Municipality, MunicipalityXRegion


def index(request):
    regions = Region.objects.all()
    municipalities = Municipality.objects.all()
    context = {
        'regions': regions,
        'municipalities': municipalities,
    }
    return render(request, 'municipalities/index.html', context)


def detail_municipalities(request, m_id):
    municipality = get_object_or_404(Municipality, pk=m_id)
    context = {'municipality': municipality}
    return render(request, 'municipalities/detail.html', context)


def detail_regions(request, r_id):
    region = get_object_or_404(Region, pk=r_id)
    context = {'region': region}
    return render(request, 'municipalities/detail.html', context)


def add_municipality(request):
    if request.method == "GET":
        return render(request, 'municipalities/add_municipality.html', {})
    elif request.method == "POST":
        m_code = int(request.POST['municipality_code'])
        m_name = request.POST['municipality_name']
        m_state = request.POST['stateRadio']
        m = Municipality(code=m_code, name=m_name, state=m_state)
        m.save()
        return HttpResponseRedirect(reverse('municipalities:index'))


def edit_municipality(request, m_id):
    municipality = get_object_or_404(Municipality, pk=m_id)
    if request.method == "GET":
        context = {'municipality': municipality}
        return render(request, 'municipalities/edit_municipality.html', context)
    elif request.method == "POST":
        if 'municipality_name' in request.POST:
            if request.POST['municipality_name'] != "":
                municipality.name = request.POST['municipality_name']
        municipality.state = request.POST['stateRadio']
        if municipality.state == 'U':
            for i in Region.objects.all():
                for j in i.municipalities.all():
                    if j.code == municipality.code:
                        i.municipalities.remove(municipality)
        municipality.save()
        return HttpResponseRedirect(reverse('municipalities:index'))


def delete_municipality(request, m_id):
    if request.method == "POST":
        m = get_object_or_404(Municipality, pk=m_id)
        m.delete()
    return HttpResponseRedirect(reverse('municipalities:index'))


def edit_region(request, r_id):
    region = get_object_or_404(Region, pk=r_id)
    municipalities = Municipality.objects.all()
    if request.method == "GET":
        context = {'region': region, 'municipalities': municipalities}
        return render(request, 'municipalities/edit_region.html', context)
    elif request.method == "POST":
        if 'region_name' in request.POST:
            if request.POST['region_name'] != "":
                region.name = request.POST['municipality_name']
        if request.POST.getlist('municipalitiesSelect'):
            for i in request.POST.getlist('municipalitiesSelect'):
                municipality = get_object_or_404(Municipality, pk=i)
                m = MunicipalityXRegion(municipality=municipality, region=region)
                m.save()
        if request.POST.getlist('deleteMunicipalitiesSelect'):
            for i in request.POST.getlist('deleteMunicipalitiesSelect'):
                municipality = get_object_or_404(Municipality, pk=i)
                region.municipalities.remove(municipality)
        region.save()
        return HttpResponseRedirect(reverse('municipalities:index'))


def delete_region(request, r_id):
    if request.method == "POST":
        r = get_object_or_404(Region, pk=r_id)
        r.delete()
    return HttpResponseRedirect(reverse('municipalities:index'))


def add_region(request):
    if request.method == "GET":
        m = Municipality.objects.all()
        return render(request, 'municipalities/add_region.html', {'municipalities': m})
    elif request.method == "POST":
        r_code = int(request.POST['region_code'])
        r_name = request.POST['region_name']
        r = Region(code=r_code, name=r_name)
        r.save()
        for i in request.POST.getlist('municipalitiesSelect'):
            municipality = get_object_or_404(Municipality, pk=i)
            m = MunicipalityXRegion(municipality=municipality, region=r)
            m.save()
        return HttpResponseRedirect(reverse('municipalities:index'))

