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
# Show list of items
##################################################

@view_function
def process_request(request):
    params = {}

    # get the items in the shopping cart in an ajax ($.loadmodal) dialog

    return templater.render_to_response(request, 'shopping_cart.html', params)

@view_function
def add(request):
    params = {}

    # get the items in the shopping cart in an ajax ($.loadmodal) dialog

    return templater.render_to_response(request, 'shopping_cart.html', params)