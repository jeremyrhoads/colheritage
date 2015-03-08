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
# Show list of items to be bought
##################################################

@view_function
def process_request(request):

    if not request.user.is_authenticated():
        return redirect('/account/index/?next=%s' % request.path)

    params = {}

    user = request.user

    form = checkoutForm()

    if request.method == 'POST':
        form = checkoutForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            user.save();
            return HttpResponseRedirect('/catalogue/checkout/${ user.id }')

    # add params
    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'checkout.html', params)

class checkoutForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True, max_length=100)
    billing_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=30)
    state = forms.CharField(max_length=2)
    zip = forms.IntegerField()
    country = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=12)
    credit_card = forms.CharField(min_length=16)
    csv = forms.CharField(max_length=3)


