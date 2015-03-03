__author__ = 'MCR'

from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth import authenticate, login, logout
import homepage.models as hmod

templater = get_renderer('account')

########################################################
# signup
########################################################

@view_function
def process_request(request):
    params = {}

    # form = SignupForm()

    # params['form'] = form

    return templater.render_to_response(request, 'signup.html', params)

'''
class SignupForm(forms.Form):
    username = forms.CharField(required=True, min_length=1, max_length=100, label="Username", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Pick a username'}))

    email = forms.CharField(required=True, min_length=1, max_length=100, label="Email", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your email'}))
    password = forms.CharField(required=True, min_length=1, max_length=100, label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Create a password'}))
    '''

########################################################
# check to see if the username is available
########################################################

@view_function
def check_username(request):
    params = {}

    username = request.REQUEST.get('u')

    # print('>>>>', username)

    # check that username
    # TODO figure out how to flag existing users
    try:
        existing_user = hmod.User.objects.get(username=username)
        if username == existing_user.username:
            return HttpResponse('0')
    except hmod.User.DoesNotExist:
        return HttpResponse('1')

    # return HttpResponse('HEY WORLD')

    return templater.render_to_response(request, 'signup.html', params)