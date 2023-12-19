from django.contrib import admin

# Register your models here.
from . models import *
# Register your models here.
# admin.site.register(Woman_item)
# admin.site.register(Man_item)
# admin.site.register(Kids_item)
# admin.site.register(Transaction)
# admin.site.register(Customer)
# admin.site.register(Orderplace)
admin.site.register(Profile)

@admin.register(Woman_item)
class Woman_itemAdmin(admin.ModelAdmin):
    list_display=['id','Name','Category','image','Price','Quantity']

@admin.register(Man_item)
class Woman_itemAdmin(admin.ModelAdmin):
    list_display=['id','Name','Category','image','Price','Quantity']

@admin.register(Kids_item)
class Woman_itemAdmin(admin.ModelAdmin):
    list_display=['id','Name','Category','image','Price','Quantity']

@admin.register(Orderplace)
class OrderplaceAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','order_date','quantity','status']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=['cat_id','user','cat','purchased_quan','date']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['name','user','locality','city','zipcode','state']

@admin.register(ItemModel)
class ItemModelAdmin(admin.ModelAdmin):
    list_display=['name','amount','order_id','razorpay_payment_id','paid']

# class Profile(admin.ModelAdmin):
    # list_display=['name','email','age','gendar','mobile','image']    



from django.contrib.sessions.models import Session
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)


