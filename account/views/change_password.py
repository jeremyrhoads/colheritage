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

    user = hmod.User.objects.get(id=request.urlparams[0])

    form = passwordForm()

    if request.method == 'POST':
        form = passwordForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            user.set_password(form.cleaned_data['password2'])
            user.save()
            return HttpResponseRedirect("/account/change_password/${ user.id }")

    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'change_password.html', params)


class passwordForm(forms.Form):
    password = forms.CharField(required=True, min_length=1, max_length=100, label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True, min_length=1, max_length=100, label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    '''validate username field'''
    def clean_password(self):

        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Make sure your passwords match')
        return self.cleaned_data['password2']
