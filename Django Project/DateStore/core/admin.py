from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(order)
admin.site.register(date)
admin.site.register(imgaes) 
admin.site.register(Profile) 

#compined profile with user info
class ProfileInline(admin.StackedInline):
    model=Profile
#extend the user  model
class UserAdmin(admin.ModelAdmin):
    model=User
    field=["username","first_name","last_name","email"]
    inlines=[ProfileInline]

admin.site.unregister(User)

admin.site.register(User,UserAdmin)
