__author__ = 'MCR'

from django.contrib.auth.decorators import permission_required
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django import forms
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')

##################################################
# Shows a list of venues
##################################################

@view_function
def process_request(request):
    params = {}

    venues = hmod.Venue.objects.all().order_by('id')

    params['venues'] = venues

    return templater.render_to_response(request, 'venues.html', params)


##################################################
# Edit Venue
##################################################
@view_function
def edit(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')
    params ={}

    try:
        venue = hmod.Venue.objects.get(id=request.urlparams[0])
    except hmod.Venue.DoesNotExist:
        return HttpResponseRedirect('/homepage/venues/')

    form = VenueEditForm(initial={
            'name': venue.name,
            'address': venue.address,
            'city': venue.city,
            'state': venue.state,
            'zip': venue.zip,
            'event': venue.event,
    })

    if request.method == 'POST':
        form = VenueEditForm(request.POST)
        form.venueid = venue.id
        if form.is_valid():
            venue.name = form.cleaned_data['name']
            venue.address = form.cleaned_data['address']
            venue.city = form.cleaned_data['city']
            venue.state = form.cleaned_data['state']
            venue.zip = form.cleaned_data['zip']
            venue.event = form.cleaned_data['event']
            venue.save()
            return HttpResponseRedirect('/homepage/venues/')

    params['form'] = form
    params['venue'] = venue
    return templater.render_to_response(request, 'venues.edit.html', params)


class VenueEditForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zip = forms.CharField(max_length=100)
    event = forms.ModelChoiceField(required=False, queryset=hmod.Event.objects.all())


##################################################
# Create a new venue
##################################################

@view_function
def create(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    venue = hmod.Venue()

    venue.name = ''
    venue.address = ''
    venue.city = ''
    venue.state = ''
    venue.zip = 12345
    # venue.event = '' this needs to be an instance of the event model for the db to accept

    venue.save()

    return HttpResponseRedirect('/homepage/venues.edit/{}/'.format(venue.id))


##################################################
# Delete a venue hehe
##################################################

@view_function
def delete(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    try:
        venue = hmod.Venue.objects.get(id=request.urlparams[0])
    except hmod.Venue.DoesNotExist:
        return HttpResponseRedirect('/homepage/venues/')

    venue.delete()
    return HttpResponseRedirect('/homepage/venues/')
