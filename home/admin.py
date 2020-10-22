from django.contrib import admin
from .models import Gallery, Posts

admin.site.site_header = "You Were Chosen"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to the YWC admin area"


# Register your models here.
admin.site.register(Gallery)
admin.site.register(Posts)
