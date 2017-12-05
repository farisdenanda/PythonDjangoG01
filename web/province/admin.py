from django.contrib import admin
from orm.models import Province

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    pass