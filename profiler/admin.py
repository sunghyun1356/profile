from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    pass

class ProjectsAdmin(admin.ModelAdmin):
    pass

class ResumeAdmin(admin.ModelAdmin):
    pass



admin.site.register(Profile, ProfileAdmin)
# Register your models here.
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Resume, ResumeAdmin)
