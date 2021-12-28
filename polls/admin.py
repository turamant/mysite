from django.contrib import admin

# Register your models here.
from polls.models import Vote

admin.site.register(Vote)
