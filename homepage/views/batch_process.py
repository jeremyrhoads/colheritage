__author__ = 'MCR'

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django import forms
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from _datetime import datetime


templater = get_renderer('homepage')

##################################################
# Show list of items
##################################################

@view_function
def process_request(request):

    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    batch = hmod.Rental.objects.filter(due_date__lte=datetime.now())

    params['batch'] = batch
    return templater.render_to_response(request, 'batch_process.html', params)
