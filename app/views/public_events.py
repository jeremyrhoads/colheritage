__author__ = 'MCR'

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms
from django_mako_plus.controller import view_function
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

    pub_events = hmod.Public_Event.objects.all().order_by('id')

    params['pub_events'] = pub_events

    return templater.render_to_response(request, 'public_events.html', params)

##################################################
# Edit event
##################################################

@view_function
def edit(request):
    params = {}

    try:
        pub_event = hmod.Public_Event.objects.get(id=request.urlparams[0])
    except hmod.Public_Event.DoesNotExist:
        return HttpResponseRedirect("homepage/public_events/")

    form = PubEventEditForm(initial={
        'name': pub_event.name,
        'description': pub_event.description,
        'event': pub_event.event,

    })

    if request.method == 'POST':
        form = PubEventEditForm(request.POST)
        form.pubeventid = pub_event.id
        if form.is_valid():
            pub_event.name = form.cleaned_data['name']
            pub_event.description = form.cleaned_data['description']
            pub_event.event = form.cleaned_data['event']
            pub_event.save()
            return HttpResponseRedirect("/homepage/public_events/")

    params['form'] = form
    params['pub_event'] = pub_event
    return templater.render_to_response(request, 'public_events.edit.html', params)

class PubEventEditForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    event = forms.ModelChoiceField(required=False, queryset=hmod.Event.objects.all())


##################################################
# Create a new event
##################################################

@view_function
def create(request):

    pub_event = hmod.Public_Event()

    pub_event.name = ''
    pub_event.description = ''
    # pub_event.event =
    pub_event.save()

    pub_event.save()

    return HttpResponseRedirect('/homepage/public_events.edit/{}/'.format(pub_event.id))


##################################################
# Delete an event
##################################################

@view_function
def delete(request):

    try:
        pub_event = hmod.Public_Event.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/public_events/')

    pub_event.delete()
    return HttpResponseRedirect('/homepage/public_events/')