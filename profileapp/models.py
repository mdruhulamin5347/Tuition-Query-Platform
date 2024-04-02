from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from post.models import District
from multiselectfield import MultiSelectField

# Create your models here.

class userprofile_model(models.Model):
    GENDER_CHOICE=(
        ('Male','Male'),
        ('Female','Female')
    )


    CATAGORY=(
        ('Teacher','Teacher'),
        ('Student','Student')
    )
    BLOAD_GROUP=(
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
        ('AB+','AB+'),
        ('AB-','AB-')
    )
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    birth_date=models.DateField()
    gender=models.CharField(max_length=50,choices=GENDER_CHOICE)
    blood_group=models.CharField(max_length=50, choices=BLOAD_GROUP)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    nationality=models.CharField(max_length=50)
    religion=models.CharField(max_length=40)
    biodata=models.TextField()
    profession=models.CharField(max_length=50,choices=CATAGORY)
    image=models.ImageField(upload_to='media/profile')
    def __str__(self):
        return f"{self.user.username} Profile"
    def save(self):
        super().save()
        image=Image.open(self.image.path)
        if image.height > 300 or image.width >300:
            output=(300,300)
            image.thumbnail(output)
            image.save(self.image.path)

class Subject(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Class_in(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class teacher_model(models.Model):
    STATAS=(
        ('Available','Available'),
        ('busy','busy'),
    )
    choice_style=(
        ('Group_Tuition','Group_Tuition'),
        ('Private_Tuition','Private_Tuition'),
    )
    choice_place=(
        ('Class_rooms','Class_rooms'),
        ('Coaching_center','Coaching_center'),
        ('Home_visit','Home_visit'),
        ('My_place','My_place'),
    )
    choice_aproach=(
        ('Online_help','Online_help'),
        ('Phone_help','Phone_hlep'),
        ('Provide_Hand_Notes','Provide_Hand_Notes'),
        ('Video_Tutorials','Video_Tutorials'),

    )
    choice_medium=(
        ('Bangla_medium','Bangla_medium'),
        ('English_medium','English_medium'),
        ('Arabic_medium','Arabic_medium'),
        ('Hindi_medium','Hindi_medium'),
        ('China_medium','China_medium'),
        ('Computer learning','Computer_learning'),
        ('Language learning','Language_learning'),
    )
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_model')
    district=models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='district')
    style=MultiSelectField(max_length=50, choices=choice_style , max_choices=3)
    place=MultiSelectField(max_length=50, choices=choice_place, max_choices=3)
    aproach=MultiSelectField(max_length=50, choices=choice_aproach, max_choices=3)
    medium=MultiSelectField(max_length=50, choices=choice_medium, max_choices=4)
    subject_in=models.ManyToManyField(Subject, related_name='set_subject_in')
    class_in=models.ManyToManyField(Class_in, related_name='set_class_in')
    salary=models.IntegerField()
    days_per_week=models.CharField(max_length=50)
    education=models.CharField(max_length=50)
    statas=models.CharField(max_length=50, choices=STATAS)





            


