from django.contrib import admin

# Register your models here.
from puzzle.models import *

admin.site.register(Level)
admin.site.register(Stage)
admin.site.register(UserStage)
admin.site.register(UserLevel)