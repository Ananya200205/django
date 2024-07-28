from django.contrib import admin
from.models import Student, Course, Enrollment,Project

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
@admin.register(Project) 
class ProjectAdmin(admin.ModelAdmin): 
        list_display = ('student', 'topic', 'languages_used', 'duration') 
        search_fields = ('student__first_name', 'student__last_name', 'topic') 
