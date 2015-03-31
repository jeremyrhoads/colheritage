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

    catalogue_items = hmod.Item.objects.all().order_by('name')

    catalogue_products = hmod.Product.objects.all().order_by('name')

    print('>>>>>>>>>', request.session)


    # items = hmod.Item.objects.all().order_by('id')

    params['catalogue_items'] = catalogue_items
    params['catalogue_products'] = catalogue_products
    return templater.render_to_response(request, 'index.html', params)