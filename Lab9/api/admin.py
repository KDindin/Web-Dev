from django.contrib import admin
from api.models import Company, Vacancy

# Register your models here.

# admin.site.register(Company)
# admin.site.register(Vacancy)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "city", "address")


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "salary", "company")