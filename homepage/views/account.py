__author__ = 'MCR'

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')


@view_function
def process_request(request):
    if not request.user.is_authenticated():
        HttpResponseRedirect('/homepage/login')

    return templater.render_to_response(request, 'account.html')