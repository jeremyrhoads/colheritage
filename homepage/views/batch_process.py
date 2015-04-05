__author__ = 'MCR'

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django import forms
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import datetime
from django.core.mail import send_mail, EmailMultiAlternatives


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

    #batch = hmod.Rental.objects.filter(due_date__lte=datetime.now())
    #batch = hmod.Rental.objects.filter(return_time__isnull=True)
    #batch = db.rentedItem.objects.filter(return_time__isnull = True, and due_date__lte= datetime.now())
    #combine rental and return tables and update database
    #Get todays date
    today = datetime.datetime.now()
    thirtydays = today - datetime.timedelta(days=30)
    sixtydays = today - datetime.timedelta(days=60)
    ninetydays = today - datetime.timedelta(days=90)

    batch_30 = hmod.Rental.objects.filter(due_date__range=[thirtydays, today])

    batch_60 = hmod.Rental.objects.filter(due_date__range=[sixtydays, thirtydays])

    batch_90 = hmod.Rental.objects.filter(due_date__lte=ninetydays)

    emailbody = templater.render(request, 'batch_process.html', params)
    emailsubject = 'Over Due Items'
    from_email = 'rhoadsjmr@gmail.com'
    to_email = ['riderm17@gmail.com']

    send_mail(emailsubject, emailbody, from_email, to_email, html_message=emailbody, fail_silently=False)

    params['batch_30'] = batch_30
    params['batch_60'] = batch_60
    params['batch_90'] = batch_90

    return templater.render_to_response(request, 'batch_process.html', params)
