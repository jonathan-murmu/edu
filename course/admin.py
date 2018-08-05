from django.contrib import admin

from course.models import Course


class CourseAdmin(admin.ModelAdmin):
    fields = ['course_name']
    list_display = ('course_name', 'get_users')

    def get_users(self, obj):
        return ", ".join([c.username for c in obj.user_set.all()])

admin.site.register(Course, CourseAdmin)
