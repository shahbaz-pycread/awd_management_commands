from django.contrib import admin
from .models import Student, Customer
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','roll_no','age']
admin.site.register(Student, StudentAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'country']
    list_filter = ['country']
    search_fields = ['country']
    
admin.site.register(Customer, CustomerAdmin)
