from django.contrib import admin
from . models import Department, Role, Employee, Register
# Register your models here.


admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Register)