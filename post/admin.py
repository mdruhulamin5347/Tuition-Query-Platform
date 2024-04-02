from django.contrib import admin
from .models import post_model,Teacher,Student,Comment,photo_add_model,District
from django.utils import timezone
from django.utils.html import format_html


admin.site.site_header='Ruhul Admin Panel'
admin.site.site_title='Ruhul Admin Panel'
admin.site.index_title=''

class commentinline(admin.TabularInline):
    model=Comment

class photo_inline(admin.TabularInline):
    model=photo_add_model

class postAdmin(admin.ModelAdmin):
    #fields=('title','salary')
    #exclude=('user','create_at')
    readonly_fields=('slug',)
    list_display=('user','title_html_display','title','get_teacher','get_student','salary','created_since',)
    list_filter=('title','teacher','student',)
    search_fields=('title','user__username','salary','teacher__name','student__name')
    list_editable=('salary',)
    list_display_links=('title',)
    filter_horizontal=('teacher','student')
    actions=('change_salary_300',)
    inlines=[commentinline,photo_inline,]


    def created_since(self,post_model):
        diff=timezone.now() - post_model.create_at
        return diff.days
    created_since.short_description='Create Since'

    def get_teacher(self,obj):
        return ", ".join([p.name for p in obj.teacher.all()])
    get_teacher.short_description='Teacher'
    def get_student(self, obj):
        return ",".join([p.name for p in obj.student.all()])
    get_student.short_description='Student'

    def title_html_display(self,obj):
        return format_html(
            f'<spam style="color:aqua; font-size:20px;">{obj.title}</spam>'
        )




    def change_salary_300(self, request, queryset):
        count=queryset.update(salary=3000.0)
        self.message_user(request,'{},posts update' .format(count))

# Register your models here.
admin.site.register(post_model,postAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Comment)
admin.site.register(photo_add_model)
admin.site.register(District)
