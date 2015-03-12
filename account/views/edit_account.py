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

##################################################
# Edit a user
##################################################

@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return redirect('/homepage/login/?next=%s' % request.path)

    params = {}

    user = request.user

    form = UserEditForm(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'address': user.address,
        'city': user.city,
        'state': user.state,
        'zip': user.zip,
        'country': user.country,
        'telephone': user.telephone,

        'date_joined': user.date_joined,
        'last_login': user.last_login,
        'username': user.username,
        'security_question': user.security_question,
        'is_staff': user.is_staff,
        'is_active': user.is_active,
        'image': user.image,

    })

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.address = form.cleaned_data['address']
            user.city = form.cleaned_data['city']
            user.state = form.cleaned_data['state']
            user.zip = form.cleaned_data['zip']
            user.country = form.cleaned_data['country']
            user.telephone = form.cleaned_data['telephone']
            user.date_joined = form.cleaned_data['date_joined']
            user.last_login = form.cleaned_data['last_login']
            user.username = form.cleaned_data['username']
            user.security_question = form.cleaned_data['security_question']
            user.is_staff = form.cleaned_data['is_staff']
            user.is_active = form.cleaned_data['is_active']
            user.image = form.cleaned_data['image']
            user.save()
            return HttpResponseRedirect("/homepage/users/")

    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'edit_account.html', params)


class UserEditForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True, max_length=100)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=30)
    state = forms.CharField(max_length=2)
    zip = forms.IntegerField()
    country = forms.CharField(max_length=30)
    telephone = forms.CharField(max_length=12)

    date_joined = forms.DateField()
    last_login = forms.DateTimeField()
    username = forms.CharField(label='Username *', required=True, max_length=100)
    security_question = forms.CharField(required=True, max_length=100)
    is_staff = forms.CharField(max_length=100)
    is_active = forms.CharField(max_length=100)
    image = forms.CharField(max_length=100)

    '''validate username field'''
    def clean_username(self):

        if len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError('Please enter a username that is 5 characters or longer')

        users = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid)
        if len(users) >= 1:
            raise forms.ValidationError('This username is already taken!!! Choose a different one')

        return self.cleaned_data['username']
