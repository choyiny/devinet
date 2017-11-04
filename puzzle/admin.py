from django.contrib import admin

# Register your models here.
from puzzle.models import Level, Stage

admin.site.register(Level)
admin.site.register(Stage)