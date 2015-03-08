__author__ = 'MCR'

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django import forms
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer


templater = get_renderer('catalogue')

##################################################
# Show item details
##################################################

@view_function
def process_request(request):
    params = {}

    item = hmod.Item.objects.get(id=request.urlparams[0])


    params['item'] = item
    return templater.render_to_response(request, 'item-details.html', params)