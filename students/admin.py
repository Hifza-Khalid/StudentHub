from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'course']
    list_filter = ['course', 'age']
    search_fields = ['name', 'email', 'course']
    list_per_page = 20
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'age')
        }),
        ('Academic Information', {
            'fields': ('course',)
        }),
    )