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

    rentals = hmod.Rental.objects.all().order_by('due_date')

    # for r in rentals:
    # print(r)

    params['rentals'] = rentals
    return templater.render_to_response(request, 'rentals.html', params)


@view_function
def returns(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    params = {}

    rental = hmod.Rental.objects.get(id=request.urlparams[0])
    employee = request.user.get_full_name()
    return_date = datetime.datetime.now()


    params['rental'] = rental
    params['employee'] = employee
    params['return_date'] = return_date
    return templater.render_to_response(request, 'rentals.returns.html', params)


@view_function
def return_complete(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)
    if not request.user.is_staff:
        return HttpResponseRedirect('/homepage/authentication')

    current_employee = hmod.User.objects.get(id=request.user.id)

    # create a new return object
    new_r = hmod.Return()
    new_r.return_time = datetime.datetime.now()
    new_r.fees_paid = "10.00"
    new_r.handled_by = current_employee
    new_r.save()

    # delete that rental for now, you should archive it though
    # TODO this should actually just turn off an is_rented boolean so we don't have to delete the data
    rental = hmod.Rental.objects.get(id=request.urlparams[0])
    rental.delete()

    return HttpResponseRedirect('/homepage/rentals')