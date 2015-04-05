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
# Show list of items
##################################################

@view_function
def process_request(request):
    params = {}

    # get the items in the shopping cart in an ajax ($.loadmodal) dialog

    return templater.render_to_response(request, 'shopping_cart.html', params)

@view_function
def add(request):
    params = {}

    # get the items in the shopping cart in an ajax ($.loadmodal) dialog
    itemid = request.urlparams[0]
    qty = request.urlparams[1]
    type = request.urlparams[2]

    # print(itemid + qty + type)

    items = {}
    products = {}

    items_cart = {}
    products_cart = {}

    if itemid and qty:
        if type == "rental":
            # do we have a shopping cart named items_cart yet
            if 'items_cart' not in request.session:
                request.session['items_cart'] = {}

            items_cart = request.session.get('items_cart', {})
            # print("new session object")

            if itemid in items_cart:
                # add the item and its quantity to the cart, updating the cart
                items_cart[itemid] = int(items_cart[itemid]) + int(qty)
            else:
                # creates a new item and its quantity
                items_cart[itemid] = int(qty)
                # print('qty assigned')

            # save the cart back to the session
            request.session['items_cart'] = items_cart

        else:
            # do we have a shopping cart named products_cart yet
            if 'products_cart' not in request.session:
                request.session['products_cart'] = {}

            products_cart = request.session.get('products_cart', {})

            if itemid in products_cart:
                # add the item and its quantity to the cart, updating the cart
                products_cart[itemid] = int(products_cart[itemid]) + int(qty)
            else:
                # creates a new item and its quantity
                products_cart[itemid] = int(qty)
                # print('qty assigned')

            # save the cart back to the session
            request.session['products_cart'] = products_cart

        # get ready to send back to the view
        items_cart = request.session.get('items_cart', {})
        products_cart = request.session.get('products_cart', {})
        amt = 0

        # for each item in the cart, add each one to the items dictionary for use in the template
        for item in hmod.Item.objects.filter(id__in=items_cart.keys()):
            items[str(item.id)] = item

        # for each item in the cart, add each one to the items dictionary for use in the template
        for product in hmod.Product.objects.filter(id__in=products_cart.keys()):
            products[str(product.id)] = product

        # for each item, calc the total
        for key in items:
            i = items[key]
            amt += i.standard_rental_price * items_cart[str(i.id)]

        # for each product, calc the total
        for key in products:
            i = products[key]
            amt += i.current_price * products_cart[str(i.id)]

        # load params
        params = {
            'items': items,
            'items_cart': items_cart,
            # do the same for products
            'products': products,
            'products_cart': products_cart,
            'amt': amt
        }

    return templater.render_to_response(request, 'shopping_cart.html', params)


@view_function
def delete(request):
    params = {}

    # get the items in the shopping cart in an ajax ($.loadmodal) dialog
    itemid = request.urlparams[0]
    type = request.urlparams[1]

    items = {}
    products = {}

    items_cart = {}
    products_cart = {}

    if type == "rental":
        # get the cart from the session
        items_cart = request.session.get('items_cart', {})
        print('>>>>>>>>>>>>>>>>> item cart loaded')
        # pop the item off of the dictionary
        items_cart.pop(itemid)

        # update the cart
        request.session['items_cart'] = items_cart

    # else do the same for products
    else:
        # get the cart from the session
        products_cart = request.session.get('products_cart', {})
        print('>>>>>>>>>>>>>>>>> product cart loaded')
        # pop the item off of the dictionary
        products_cart.pop(itemid)
        print('>>>>>>>>>>>>>>>>> popped')

        # update the cart
        request.session['products_cart'] = products_cart

    # get ready to send back to the view
    items_cart = request.session.get('items_cart', {})
    products_cart = request.session.get('products_cart', {})
    amt = 0

    # for each item in the cart, add each one to the items dictionary for use in the template
    for item in hmod.Item.objects.filter(id__in=items_cart.keys()):
        items[str(item.id)] = item

    # for each item in the cart, add each one to the items dictionary for use in the template
    for product in hmod.Product.objects.filter(id__in=products_cart.keys()):
        products[str(product.id)] = product

    # for each item, calc the total
    for key in items:
        i = items[key]
        amt += i.standard_rental_price * items_cart[str(i.id)]

    # for each product, calc the total
    for key in products:
        i = products[key]
        amt += i.current_price * products_cart[str(i.id)]

    # load params
    params = {
        'items': items,
        'items_cart': items_cart,
        # do the same for products
        'products': products,
        'products_cart': products_cart,
        'amt': amt
    }

    return templater.render_to_response(request, 'shopping_cart.html', params)