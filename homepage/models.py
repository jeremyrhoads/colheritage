__author__ = 'MCR'

from django.db import models
from django.contrib.auth.models import AbstractUser

#####################################
# User Class extends AbstractUser
#####################################

class User(AbstractUser):
    '''
    INHERITED FIELDS
    # password
    # last_login
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined
    '''
    address = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    telephone = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True)
    security_question = models.TextField(null=True, blank=True)
    security_answer = models.TextField(null=True, blank=True)
    org_name = models.TextField(null=True, blank=True)
    org_type = models.TextField(null=True, blank=True)
    emergency_contact = models.TextField(null=True, blank=True)
    emergency_phone = models.IntegerField(null=True, blank=True)
    emergency_relationship = models.TextField(null=True, blank=True)


class Photograph(models.Model):
    date_taken = models.DateField()
    place_taken = models.TextField(max_length=50)
    Image = models.ImageField()


class Phone(models.Model):
    number = models.TextField(max_length=15)
    extension = models.IntegerField()
    type = models.TextField(max_length = 30)
    employee = models.ForeignKey('User', null=True)


class Item(models.Model):
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=50)
    value = models.IntegerField()
    standard_rental_price = models.DecimalField(max_digits=5, decimal_places = 2)
    owner = models.ForeignKey('User', null= True)


class Wardrobe_Item(Item):
    size = models.TextField(max_length=10)
    size_modifier = models.TextField(max_length=30)
    gender = models.TextField(max_length=10)
    color = models.TextField(max_length=20)
    pattern = models.TextField(max_length=20)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    note = models.TextField(max_length=80)


class Product(models.Model):
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=50)
    category = models.TextField(max_length=15)
    current_price = models.FloatField()
    owner = models.ForeignKey('User')


class Product_Picture(models.Model):
    picture = models.ImageField()
    caption = models.TextField(max_length=30)
    product = models.ForeignKey('Product')


class Cart_Product(models.Model):
    quantity = models.IntegerField()


class Cart_Item(models.Model):
    quantity = models.IntegerField()


class Bulk_Product(Product):
    quantity_on_hand = models.IntegerField()


class Personal_Product(Product):
    order_form_name = models.TextField(max_length=20)
    production_Time = models.TimeField()


class Order(models.Model):
    order_date = models.DateField()
    phone = models.IntegerField()
    date_packed = models.DateField()
    date_paid = models.DateField()
    date_shipped = models.DateField()
    tracking_number = models.IntegerField()
    shipped_by = models.ForeignKey('User', null= True, related_name= 'shipper')
    processed_by = models.ForeignKey('User', null= True, related_name= 'processor')
    packed_by = models.ForeignKey('User', null= True, related_name= 'packer')
    customer = models.ForeignKey('User', null= True)
    bulk_product_count = models.ManyToManyField('Bulk_Product', null= True, through='Bulk_Detail')
    personal_product_count = models.ManyToManyField('Personal_Product', null= True, through='Personal_Detail')


class Individual_Product(Product):
    date_made = models.DateField()
    on_order = models.ForeignKey('Order', null= True)


class Area(models.Model):
    name = models.TextField(max_length=40)
    description = models.TextField(max_length=50)
    place_number = models.IntegerField()
    coordinator = models.ForeignKey('User', null= True, related_name='coordinates')
    supervised_by = models.ForeignKey('User', null= True, related_name= 'supervises')


class Sale_Item(models.Model):
    name = models.TextField(max_length=40)
    description = models.TextField(max_length=50)
    low_price = models.FloatField()
    high_price = models.FloatField()
    area = models.ForeignKey('Area', null= True)


class Event(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    map_file_name = models.TextField(max_length=30)


class Public_Event(models.Model):
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=50)
    event = models.ForeignKey('Event', null= True)


class Venue(models.Model):
    name = models.TextField(max_length=30)
    address = models.TextField(max_length=40)
    city = models.TextField(max_length=40)
    state = models.TextField(max_length=3)
    zip = models.IntegerField()
    event = models.ForeignKey('Event', null= True)


class Rentable_Item(Item):
    pass


class Photographable_Thing(models.Model):
    photograph = models.ManyToManyField('Photograph')


class Rental(models.Model):
    rental_time = models.TimeField()
    due_date = models.DateField()
    discount_percent = models.FloatField()
    customer = models.ForeignKey('User', null= True)
    items_rented = models.ManyToManyField('Rentable_Item', through='Rented_Item')


class Return(models.Model):
    return_time = models.TimeField()
    fees_paid = models.FloatField()
    handled_by = models.ForeignKey('User')


class Rented_Item(models.Model):
    rentable_item = models.ForeignKey('Rentable_Item')
    rental = models.ForeignKey('Rental')
    condition = models.TextField()
    new_damage = models.TextField()
    damage_fee = models.FloatField()
    late_fee = models.FloatField()
    return_number = models.ForeignKey('Return')


class Bulk_Detail(models.Model):
    bulk_product = models.ForeignKey('Bulk_Product')
    order = models.ForeignKey('Order')
    quantity = models.IntegerField()
    price = models.FloatField()


class Personal_Detail(models.Model):
    personal_product = models.ForeignKey('Personal_Product')
    order = models.ForeignKey('Order')
    order_file = models.TextField()


class Role(models.Model):
    participant = models.ForeignKey('User')
    area = models.ForeignKey('Area')
    name = models.TextField()
    type = models.TextField()
