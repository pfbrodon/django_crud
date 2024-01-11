from django.contrib import admin
from .models import Task #importa la tabla Task desde models

class TaskAdmin(admin.ModelAdmin):
    readonly_fields=('created',) # indico los campos de solo lectura
# Register your models here.
admin.site.register(Task, TaskAdmin) 
