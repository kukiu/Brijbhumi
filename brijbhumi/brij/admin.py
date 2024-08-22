from django.contrib import admin
from .models import Brajbhumi


@admin.register(Brajbhumi)
class Brajadmin(admin.ModelAdmin):
    list_display=['name','lastname','phone','choice','textfield','created_at']