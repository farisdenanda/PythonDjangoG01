from django.contrib import admin
from orm.models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass