from django.contrib import admin

from .models import Profile, Product, Address


admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Address)
