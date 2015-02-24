__author__ = 'MCR'


from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')


@view_function
def process_request(request):

    return templater.render_to_response(request, 'authentication.html')