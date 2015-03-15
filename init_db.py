__author__ = 'MCR'

#!/usr/bin/env python3

# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'sprint2.settings'
import django
django.setup()

# regular imports
from django.contrib.auth import models as conmod
import homepage.models as hmod
import datetime

from django.contrib.auth.models import Group, Permission, ContentType


# drop the tables


# create users with groups and permissions
for data in[
    ['adminUser', 'password', True, True, 'Ratt', 'Mider', '123@abc.com', True, datetime.datetime.now(), 'Admin', 7, 'Super Privileges', 'Admin', 94],
    ['staffUser', 'password', False, True, 'Rheremy', 'Joads', '123@abc.com', True, datetime.datetime.now(), 'Manager', 7, 'Manager Privileges', 'Manager', 95],
    ['guestUser1', 'password', False, False, 'Baylor', 'Tarrowes', '123@abc.com', True, datetime.datetime.now(), 'User', 7, 'Guest Privileges', 'User', 96],
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

# create events
for data in [
    ['event_map1.jpeg'],
    ['event_map2.jpeg'],
    ['event_map3.jpeg'],
]:
    event = hmod.Event()
    event.start_date = datetime.datetime.now()
    event.end_date = datetime.datetime.now()
    event.map_file_name = data[0]
    event.save()


# create public events
for data in [
    ['Pie eating contest', 'See who can eat the most apple pies'],
    ['Storytelling', 'Hear Ben Franklin read his favorite stories to children'],
    ['Marksmen contest', 'See who the best musket shot'],
]:
    pub_event = hmod.Public_Event()
    pub_event.name = data[0]
    pub_event.description = data[1]
    # pub_event.event =
    pub_event.save()


# create venues
for data in [
    ['Washington Park', '123 Pres. Circle', 'SLC', 'UT'],
    ['Franklin Home', '456 Innovation Way', 'Orem', 'UT'],
    ['Jefferson Cottage', '22 Abc Rd.', 'Salem', 'UT'],
    ['Adams Distillery', '66 Wasted Dr.', 'Price', 'UT'],
]:
    venue = hmod.Venue()

    venue.name = data[0]
    venue.address = data[1]
    venue.city = data[2]
    venue.state = data[3]
    venue.zip = 12345
    # venue.event = '' this needs to be an instance of the event model for the db to accept

    venue.save()

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
    item.description = data[1]
    item.value = data[2]
    item.standard_rental_price = data[3]
    # item.owner = hmod.User.objects.get(id=1)
    item.save()


