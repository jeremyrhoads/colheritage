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
    ['adminUser', 'password', True, True, 'Ratt', 'Mider', '123@abc.com', True, datetime.datetime.now()],
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

# create group


# set permissions