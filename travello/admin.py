
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Destination

@admin.register(Destination)


class ViewAdmin(ImportExportModelAdmin):
    pass


# Register your models here.
