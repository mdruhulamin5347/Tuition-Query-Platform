from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.utils.text import slugify
from PIL import Image

# Create your models here.
class Teacher(models.Model):
    name=models.CharField( max_length=50)
    def __str__(self):
        return self.name
class Student(models.Model):
    name=models.CharField( max_length=50)
    def __str__(self):
        return self.name

class District(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name



class post_model(models.Model):
    CATAGORY=(
        ('Teacher','Teacher'),
        ('Student','Student'),
    )
    MIDDLE=(
        ('Bangla','Bangla'),
        ('English','English'),
        ('Hindi','Hindi'),
        ('Arabic','Arabic'),
   )
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    slug=models.CharField(max_length=100, default=title)
    salary=models.IntegerField()
    details=models.TextField()
    district=models.CharField(max_length=100, null=True,blank=True)
    abalable=models.BooleanField()
    catagory=models.CharField(max_length=50, choices=CATAGORY)
    middle=MultiSelectField(max_length=50,choices=MIDDLE, default='Bangla')
    teacher=models.ManyToManyField(Teacher, related_name='set_teacher')
    student=models.ManyToManyField(Student, related_name='set_student')
    image=models.ImageField(default='default.jpg',upload_to='media/images/')
    create_at=models.DateTimeField(default=now)
    likes=models.ManyToManyField(User,related_name='set_likes')
    views=models.ManyToManyField(User,related_name='set_views')
    def tatal_like(self):
        return self.likes.count()
    def total_view(self):
        return self.views.count()

    
    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(post_model,self).save(*args, **kwargs)
        image=Image.open(self.image.path)
        if image.height==300 or image.width==300:
            output=(300,300)
            image.thumbnail(output)
            image.save(self.image.path)

            
    def get_teacher_list(self):
        t=self.teacher.all()
        teachers=" "
        for s in t:
            teachers=teachers + str(s.name)+ ','
        return teachers
    def get_student_list(self):
        s=self.student.all()
        Students=" "
        for i in s:
            Students=Students + str(i.name)+ ","
        return Students
    
    def title_proper(self):
        return self.title.title()
    
    def details_short(self):
        detail_word=self.details.split(' ')
        if len(detail_word) > 3:
            return ' '.join(detail_word[:3]) + '...'
        else:
            return self.details



class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(post_model,on_delete=models.CASCADE)
    text=models.TextField()
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    create_at=models.DateTimeField(default=now)
    def __str__(self):
        return self.user.username + " : " + self.text[0:10]
    



class photo_add_model(models.Model):
    image=models.ImageField(upload_to='media/image')
    post=models.ForeignKey(post_model, on_delete=models.CASCADE, related_name='images')
    def save(self, *args, **kwargs):
        super(photo_add_model,self).save(*args, **kwargs)
        image=Image.open(self.image.path)
        if image.height > 300 or image.width > 300 :
            output=(300,300)
            image.thumbnail(output)
            image.save(self.image.path)
     



