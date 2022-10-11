from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    '''Admin View for CourseCategory'''

    list_display = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    '''Admin View for Course'''

    list_display = ('name','category','duration')
    list_filter = ('category','name')
 

admin.site.register(FAQ)
admin.site.register(Faculty_Profile)
admin.site.register(PlacementPartner)
admin.site.register(Contact)