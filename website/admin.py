from django.contrib import admin
from .models import Team, Contact

# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-"
    list_display = ("team_name", "language", "created_date")
    search_fields = ("team_name", "language")




@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-"
    list_display = ("name", "subject", "created_date", "email")
    search_fields = ("name", "subject", "message", "email")


