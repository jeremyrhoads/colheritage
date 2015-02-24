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

    products = hmod.Product.objects.all().order_by('id')
    params['products'] = products

    return templater.render_to_response(request, 'products.html', params)


##################################################
# Edit an item
##################################################

@view_function
# @permission_required('homepage.add_item')
def edit(request):
    params = {}

    try:
        product = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.Item.DoesNotExist:
        return HttpResponseRedirect('/homepage/products/')

    # read the edit form class into the form object
    form = ProductEditForm(initial={
        'name': product.name,
        'description': product.description,
        'category': product.category,
        'current_price': product.current_price,
        'owner': product.owner,
    })

    # check is valid
    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        form.itemid = product.id
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.current_price = form.cleaned_data['current_price']
            product.owner = form.cleaned_data['owner']
            product.save()
            return HttpResponseRedirect('/homepage/products/')

    params['form'] = form
    params['item'] = product
    return templater.render_to_response(request, 'products.edit.html', params)


class ProductEditForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    category = forms.CharField(max_length=50)
    current_price = forms.DecimalField(max_digits=5, decimal_places=2)
    owner = forms.ModelChoiceField(label='Owner ID', required=False, queryset=hmod.User.objects.all())


##################################################
# Create a new product
##################################################

@view_function
def create(request):

    product = hmod.Product()

    '''
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=50)
    category = models.TextField(max_length=15)
    current_price = models.FloatField()
    owner = models.ForeignKey('User') # this used to reference Legal_Entity
    '''
    product.name = ''
    product.description = ''
    product.category = 'antiques'
    product.current_price = 10
    product.owner = hmod.User.objects.get(id=1)
    product.save()

    return HttpResponseRedirect('/homepage/products.edit/{}/'.format(product.id))

##################################################
# Delete product
##################################################

@view_function
def delete(request):

    try:
        product = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/products/')

    product.delete()
    return HttpResponseRedirect('/homepage/products/')