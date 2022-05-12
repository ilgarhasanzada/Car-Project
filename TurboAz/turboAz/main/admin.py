from django.contrib import admin
from .models import Model,Car,Marka,Color,Oturucu,Suretler_qutusu,Yanacaq
# Register your models here.
admin.site.register(Marka)
admin.site.register(Model)
admin.site.register(Car)
admin.site.register(Color)
admin.site.register(Oturucu)
admin.site.register(Suretler_qutusu)
admin.site.register(Yanacaq)