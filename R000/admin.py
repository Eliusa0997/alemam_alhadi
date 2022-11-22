from django.contrib import admin
from .models import College, Department, Program, Batch, Studant, Nationality
# Register your models here.
 
admin.site.register(College)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Batch)
admin.site.register(Studant)
admin.site.register(Nationality)