__author__ = 'MCR'

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django import forms
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.core.mail import send_mail


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
    email_subject = "Your CHF Receipt"
    email_body = templater.render(request,'receipt_email.html', params)
    from_email = 'admin@colheritagefoundation.com'
    to_email = 'riderm17@gmail.com'

    send_mail(email_subject, email_body, from_email, [to_email], html_message=email_body, fail_silently=False)

    print('>>>>>>>>>>>>>>>> testing')

    return templater.render_to_response(request, 'receipt.html', params)