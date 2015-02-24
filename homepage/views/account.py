__author__ = 'MCR'

from django.shortcuts import redirect
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')


@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)

    return templater.render_to_response(request, 'account.html')