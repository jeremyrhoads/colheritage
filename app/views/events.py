__author__ = 'MCR'

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms
from django_mako_plus.controller import view_function
from django.shortcuts import redirect
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import datetime


templater = get_renderer('homepage')

##################################################
# Shows a list of users
##################################################

@view_function
def process_request(request):
    params = {}

    events = hmod.Event.objects.all().order_by('id')

    params['events'] = events

    return templater.render_to_response(request, 'events.html', params)

##################################################
# Edit event
##################################################

@view_function
def edit(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.Event.DoesNotExist:
        return HttpResponseRedirect("homepage/events/")

    form = EventEditForm(initial={
        'start_date': event.start_date,
        'end_date': event.end_date,
        'map_file_name': event.map_file_name,

    })

    if request.method == 'POST':
        form = EventEditForm(request.POST)
        form.eventid = event.id
        if form.is_valid():
            event.start_date = form.cleaned_data['start_date']
            event.end_date = form.cleaned_data['end_date']
            event.map_file_name = form.cleaned_data['map_file_name']
            event.save()
            return HttpResponseRedirect("/homepage/events/")

    params['form'] = form
    params['event'] = event
    return templater.render_to_response(request, 'events.edit.html', params)

class EventEditForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
    map_file_name = forms.CharField()


##################################################
# Create a new event
##################################################

@view_function
def create(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    event = hmod.Event()

    event.start_date = datetime.datetime.now()
    event.end_date = datetime.datetime.now()
    event.map_file_name = 'filename.txt'

    event.save()

    return HttpResponseRedirect('/homepage/events.edit/{}/'.format(event.id))


##################################################
# Delete an event
##################################################

@view_function
def delete(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    try:
        event = hmod.Event.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/events/')

    event.delete()
    return HttpResponseRedirect('/homepage/events/')