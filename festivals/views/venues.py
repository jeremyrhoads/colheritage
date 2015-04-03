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
# Show list of items
##################################################

@view_function
def process_request(request):
    params = {}

    venue_list = hmod.Venue.objects.all().order_by('id')

    # area_list = hmod.Area.objects.all().order_by('name')

    print('>>>>>>>>')


    params['venue_list'] = venue_list
    # params['area_list'] = area_list
    return templater.render_to_response(request, 'venues.html', params)