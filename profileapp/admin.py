from django.contrib import admin
from .models import userprofile_model,teacher_model,Subject,Class_in
# Register your models here.
admin.site.register(userprofile_model)
admin.site.register(teacher_model)
admin.site.register(Subject)
admin.site.register(Class_in)


