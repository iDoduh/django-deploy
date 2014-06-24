from pprint import pprint

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.conf import settings

from shop.forms import WebsiteForm
from shop.models import Website, Plan


def login(request):
    return render_to_response('shop/login.html', {}, context_instance=RequestContext(request))


@login_required
def index(request):
    websites = Website.objects.filter(user=request.user)
    return render_to_response('shop/index.html', locals(), context_instance=RequestContext(request))


@login_required
def create(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            if settings.DEBUG:
                print " === Order data === "
                pprint(form.cleaned_data)

            # Process the data in form.cleaned_data
            site = Website(
                name=form.cleaned_data['name'],
                plan=form.cleaned_data['plan'],
                domain=form.cleaned_data['domain'],
                country=form.cleaned_data['country'],
                currency=form.cleaned_data['currency'],
                user=request.user
            )
            site.save()

            #import drest, urllib2
            #from functions import generate_settings
            #
            #api = drest.API(settings.TEAMCITY_URL)
            #api.auth(settings.TEAMCITY_USERNAME, settings.TEAMCITY_PASSWORD)
            #response = api.make_request('GET',
            #                            '/action.html?add2Queue=bt6' +
            #                            '&name=site_id&value=' + str(site.pk) +
            #                            '&name=domain&value=' + site.domain +
            #                            '&name=settings&value=' + urllib2.quote(generate_settings(site)) +
            #                            '&'  # drest will add "/" at the end
            #                            )
            #
            #if response.status != 200:
            #    raise Exception("TEAMCITY API Error", response)

            # Redirect after POST
            return HttpResponseRedirect('/shop/wait/' + str(site.pk))
    else:
        form = WebsiteForm(initial={'plan': '2'})  # by default Standard
        pprint(form.errors.items())

    return render_to_response('shop/create.html', {'form': form, 'plans': Plan.objects.all()},
                              context_instance=RequestContext(request))


def create_success(request, site_id):
    """
    Teamcity callback
    """
    try:
        site = Website.objects.get(pk=site_id)
        site.created = True
        site.save()

        return HttpResponse()
    except Website.DoesNotExist:
        return HttpResponseNotFound()


@login_required
def wait(request, site_id):
    site = Website.objects.get(pk=site_id, user=request.user)
    return render_to_response('shop/wait.html', {'site': site}, context_instance=RequestContext(request))


@login_required
def delete(request, site_id):
    try:
        site = Website.objects.get(pk=site_id, user=request.user)

        #api = drest.API(settings.TEAMCITY_URL)
        #api.auth(settings.TEAMCITY_USERNAME, settings.TEAMCITY_PASSWORD)
        #response = api.make_request('GET',
        #                            '/action.html?add2Queue=bt9' +
        #                            '&name=site_id&value=' + str(site.pk) +
        #                            '&'  # drest will add "/" at the end
        #)
        #
        #if response.status != 200:
        #    raise Exception("TEAMCITY API Error", response)
        #
        #site.delete()

        return HttpResponseRedirect('/shop/')
    except Website.DoesNotExist:
        return HttpResponseNotFound()


@login_required
def check_status(request, site_id):
    site = Website.objects.get(pk=site_id)

    if site.created:
        return HttpResponse()
    else:
        return HttpResponseNotFound()


@login_required
def check_domain(request, domain):
    if Website.objects.filter(domain=domain).count() > 0:
        return HttpResponse()
    else:
        return HttpResponseNotFound()
