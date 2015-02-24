__author__ = 'MCR'

from django.conf import settings
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpResponse
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer


@view_function
def process_request(request):
    # check user permissions and prepare params
    params = {}

templater = get_renderer('homepage')


