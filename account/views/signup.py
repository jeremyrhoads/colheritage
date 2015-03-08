__author__ = 'MCR'

from django.contrib.auth.decorators import permission_required
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django import forms
from django_mako_plus.controller import view_function
from django.contrib.auth.models import Group, Permission
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import datetime

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


##################################################
# Create new user
##################################################
@view_function
# @permission_required('homepage.add_user') # permissions id = 103
def create(request):
    params = {}

    '''Creates a new user'''
    user = hmod.User()
    # group = Group.objects.get(name='User')  # set the user to User perms by default

    user.set_password(request.urlparams[3])
    user.last_login = datetime.datetime.now()
    user.username = request.urlparams[1]
    user.first_name = ''
    user.last_name = ''
    user.email = request.urlparams[0]
    user.is_staff = False
    user.is_active = True
    user.date_joined = datetime.datetime.now()
    user.address = ''
    user.city = ''
    user.state = ''
    user.zip = 12345
    user.country = ''
    user.phone = 12345
    user.image = ''
    user.security_question = ''


    user.save()
    # group.user_set.add(user)

    return HttpResponseRedirect('/account/myaccount')