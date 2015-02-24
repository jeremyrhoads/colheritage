__author__ = 'MCR'

from django.contrib.auth.decorators import permission_required
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import datetime


templater = get_renderer('homepage')

##################################################
# Show list of items
##################################################

@view_function
def process_request(request):
    params = {}

    items = hmod.Item.objects.all().order_by('id')
    params['items'] = items

    return templater.render_to_response(request, 'items.html', params)


##################################################
# Edit an item
##################################################

@view_function
# @permission_required('homepage.add_item')
def edit(request):
    params = {}

    try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
    except hmod.Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/items/')

    # read the edit form class into the form object
    form = ItemEditForm(initial={
        'name': item.name,
        'description': item.description,
        'value': item.value,
        'standard_rental_price': item.standard_rental_price,
        'owner': item.owner,
    })

    # check is valid
    if request.method == 'POST':
        form = ItemEditForm(request.POST)
        form.itemid = item.id
        if form.is_valid():
            item.name = form.cleaned_data['name']
            item.description = form.cleaned_data['description']
            item.value = form.cleaned_data['value']
            item.standard_rental_price = form.cleaned_data['standard_rental_price']
            item.owner = form.cleaned_data['owner']
            item.save()
            return HttpResponseRedirect('/homepage/items/')

    params['form'] = form
    params['item'] = item
    return templater.render_to_response(request, 'items.edit.html', params)


class ItemEditForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    value = forms.IntegerField()
    standard_rental_price = forms.DecimalField(max_digits=5, decimal_places=2)
    owner = forms.ModelChoiceField(label='Owner ID', required=False, queryset=hmod.User.objects.all())


##################################################
# Create a new item
##################################################

@view_function
def create(request):

    item = hmod.Item()

    item.name = ''
    item.description = ''
    item.value = 0
    item.standard_rental_price = 0
    # item.owner = hmod.User.objects.get(id=1)
    item.save()

    return HttpResponseRedirect('/homepage/items.edit/{}'.format(item.id))

##################################################
# Delete item
##################################################

@view_function
def delete(request):

    try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/items/')

    item.delete()
    return HttpResponseRedirect('/homepage/items/')