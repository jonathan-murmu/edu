from django.contrib import admin

from accounts.models import User

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'course']
    list_display = ('username', 'get_course')

    def get_course(self, obj):
        return ", ".join([c.course_name for c in obj.course.all()])

admin.site.register(User, UserAdmin)