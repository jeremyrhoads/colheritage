
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'sprint2.settings'
import django; django.setup()
import homepage.models as hmod
import datetime

from django.contrib.auth.models import Group, Permission, ContentType

permission = Permission()
permission.codename = 'Admin'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Super Privileges'
permission.save()

group = Group()
group.name = "Admin"
group.save()
group.permissions.add(permission)
permission = Permission.objects.get(id=94)
group.permissions.add(permission)

user = hmod.User()
user.username = 'AdminUser'
user.set_password('asdf')
user.is_superuser = True
user.is_staff = True
user.first_name = ''
user.last_name = ''
user.email = ''
user.is_active = True
user.date_joined = datetime.datetime.now()
user.save()

group.user_set.add(user)


permission = Permission()
permission.codename = 'Manager'
permission.content_type = ContentType.objects.get(id=7) #
permission.name = 'Manager'
permission.save()

group = Group()
group.name = "Manager"
group.save()
group.permissions.add(permission)
permission = Permission.objects.get(id=95) #
group.permissions.add(permission)

user = hmod.User()
user.username = 'ManagerUser'
user.set_password('asdf')
user.is_superuser = False
user.is_staff = True
user.first_name = ''
user.last_name = ''
user.email = ''
user.is_active = True
user.date_joined = datetime.datetime.now()
user.save()

group.user_set.add(user)


permission = Permission()
permission.codename = 'User'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Guest Privileges'
permission.save()

group = Group()
group.name = "User"
group.save()
group.permissions.add(permission)
permission = Permission.objects.get(id=96)
group.permissions.add(permission)

user = hmod.User()
user.username = 'User'
user.set_password('asdf')
user.is_superuser = False
user.is_staff = False
user.first_name = ''
user.last_name = ''
user.email = ''
user.is_active = True
user.date_joined = datetime.datetime.now()
user.save()

group.user_set.add(user)