__author__ = 'MCR'

#!/usr/bin/env python3

# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django
django.setup()

# regular imports
from django.contrib.auth import models as conmod
import homepage.models as hmod
import datetime

from django.contrib.auth.models import Group, Permission, ContentType


# drop the tables


# create users
for data in[
    ['adminUser', 'password', True, True, 'Ratt', 'Mider', '123@abc.com', True, datetime.datetime.now(), 'Admin', 7, 'Super Privileges', 'Admin', 94],
    ['staffUser', 'password', False, True, 'Rheremy', 'Joads', '123@abc.com', True, datetime.datetime.now()],
    ['guestUser1', 'password', False, False, 'Baylor', 'Tarrowes', '123@abc.com', True, datetime.datetime.now()],
    ['guestUser2', 'password', False, False, 'Gill', 'Wates', '123@abc.com', True, datetime.datetime.now()],
]:
    user = hmod.User()
    user.username = data[0]
    user.set_password(data[1])
    user.is_superuser = data[2]
    user.is_staff = data[3]
    user.first_name = data[4]
    user.last_name = data[5]
    user.email = data[6]
    user.is_active = data[7]
    user.date_joined = data[8]
    user.save()

    permission = Permission()
    permission.codename = data[9]
    permission.content_type = ContentType.objects.get(id=data[10])
    permission.name = data[11]
    permission.save()

    group = Group()
    group.name = data[12]
    group.save()
    group.permissions.add(permission)
    permission = Permission.objects.get(id=data[13])
    group.permissions.add(permission)

    group.user_set.add(user)  # assign the user to the group



# create permissions and groups
'''
for data in[
    ['Admin', 7, 'Super Privileges', 'Admin', 94],
    ['Manager', 7, 'Manager Privileges', 'Manager', 95],
    ['Guest', 7, 'Guest Privileges', 'Guest', 96]
]:
    permission = Permission()
    permission.codename = data[0]
    permission.content_type = ContentType.objects.get(id=data[1])
    permission.name = data[2]
    permission.save()

    group = Group()
    group.name = data[3]
    group.save()
    group.permissions.add(permission)
    permission = Permission.objects.get(id=data[4])
    group.permissions.add(permission)
    group.user_set.add(user)
'''

# create groups
'''
for data in[
    ['Admin'],
    ['Manager'],
    ['User'],
]:
    group = Group()
    group.name = "Admin"
    group.save()
    group.permissions.add(permission)
    permission = Permission.objects.get(id=94)
    group.permissions.add(permission)
'''

# set permissions


# create events


# create public events


# create venues


# create items
for data in[
    ['Battle musket', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit', 12, 15.00],
    ['Colonial robe', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit', 50, 55.00],
    ['Pocket watch', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit', 35, 45.00],
    ['Replica telescope', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit', 72, 175.00],
    ['Teacup set', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit', 20, 25.00],
]:
    item = hmod.Item()

    item.name = data[0]
    item.description = data[0]
    item.value = data[0]
    item.standard_rental_price = data[0]
    # item.owner = hmod.User.objects.get(id=1)
    item.save()


