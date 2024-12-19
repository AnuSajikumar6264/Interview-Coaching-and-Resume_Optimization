from django.apps import AppConfig
from django.contrib import admin

class AtsSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ats_system'

    def ready(self):
        # Custom branding for the admin site
        admin.site.site_header = "ATS System Administration"
        admin.site.site_title = "ATS Admin Panel"
        admin.site.index_title = "Welcome to the ATS System Admin Dashboard"
