from django.contrib import admin
from .models import Project_add, OTPModel, Profile, Subtask

# Register your models here.
admin.site.register(Project_add)
admin.site.register(OTPModel)
admin.site.register(Profile)
admin.site.register(Subtask)
