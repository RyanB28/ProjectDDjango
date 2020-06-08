from django.contrib import admin
from .models import Profile

admin.AdminSite.site_header = "Meldkamer administratie systeem"
admin.AdminSite.site_title = "Administratie systeem"
admin.AdminSite.index_title = "Administratie"

admin.site.register(Profile)