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
from django.contrib.auth import authenticate, login, logout
import datetime

templater = get_renderer('account')

########################################################
# signup
########################################################

@view_function
def process_request(request):
    params = {}

    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            '''Creates a new user'''
            user = hmod.User()
            # group = Group.objects.get(name='User')  # set the user to User perms by default

            user.set_password(form.cleaned_data['password'])
            user.last_login = datetime.datetime.now()
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
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

            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, new_user)
            return HttpResponseRedirect("/account/myaccount")

    params['form'] = form

    return templater.render_to_response(request, 'signup.html', params)


class SignupForm(forms.Form):
    first_name = forms.CharField(required=True, min_length=1, max_length=100, label="First name", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, min_length=1, max_length=100, label="Last name", widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    username = forms.CharField(required=True, min_length=1, max_length=100, label="Username", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Pick a username', 'id': 'id_username'}))

    email = forms.CharField(required=True, min_length=1, max_length=100, label="Email", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your email'}))
    password = forms.CharField(required=True, min_length=1, max_length=100, label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Create a password'}))

    def clean_username(self):
        try:
            hmod.User.objects.get(username=self.cleaned_data['username'])
            raise forms.ValidationError('This username is already taken by another user.  Please try another.')
        except hmod.User.DoesNotExist:
            pass # this is good, username doesn't exist
        return self.cleaned_data['username']


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
        hmod.User.objects.get(username=username)
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