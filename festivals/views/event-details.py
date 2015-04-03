__author__ = 'MCR'

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django import forms
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('festivals')

##################################################
# Show item details
##################################################

@view_function
def process_request(request):
    params = {}

    event = hmod.Public_Event.objects.get(id=request.urlparams[0])

    params['event'] = event
    return templater.render_to_response(request, 'event-details.html', params)