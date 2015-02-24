__author__ = 'MCR'

from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')

##################################################
# Logout page
##################################################
@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('homepage/login/')
    else:
        logout(request)

    return templater.render_to_response(request, 'logout.html')