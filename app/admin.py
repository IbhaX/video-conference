from django.contrib import admin
from .models import Recent


@admin.register(Recent)
class RecentAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
