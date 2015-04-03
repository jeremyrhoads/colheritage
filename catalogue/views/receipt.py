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

    return templater.render_to_response(request, 'receipt.html', params)

@view_function
def email_receipt(request):
    params = {}

    # email logic goes here

    print('>>>>>>>>>>>>>>>> testing')

    return templater.render_to_response(request, 'receipt.html', params)