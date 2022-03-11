from django.conf import Settings, settings
from django.core import validators  
from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db.models.base import Model

# Create your models here.
class publisher(models.Model):
    name=models.CharField(max_length=100,null=False)
    age=models.IntegerField(null=False, validators=[MinValueValidator(19,'age must be greater than 19')])
    email=models.EmailField(help_text="enter your email",null=False)
    aadhar=models.IntegerField(validators=[MaxValueValidator(999999999999,"the adhar shouls be less than 12 digits")],unique=True)
    # user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

class post(models.Model):

    title=models.CharField(max_length=20,validators=[MinLengthValidator(2,"title must e greater than 2 characters")])
    post_image=models.ImageField(upload_to='posts/')
    caption=models.TextField(max_length=256)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class questions(models.Model):
    question_text=models.CharField(max_length=100)

    def __str__(self):
        return self.question_text

class survey(models.Model):
    question=models.ForeignKey(questions, on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    done_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)

    def __str__(self):
        return self.answer

class ask_question(models.Model):
    question=models.CharField(max_length=256)
    
    comment=models.ManyToManyField(settings.AUTH_USER_MODEL, through='comments')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.question)

class comments(models.Model):
    com=models.TextField(max_length=120, validators=[MinLengthValidator(3,"the comment lentgh must be greater than 3")], blank=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
    com_ques=models.ForeignKey(ask_question,on_delete=models.CASCADE)


class review(models.Model):
    name=models.CharField(max_length=20,validators=[MinLengthValidator(3,"please enter your full name")], null=False)
    linked_in_profile=models.URLField(help_text='please enter your linkedin id so we can connect each other')
    github=models.CharField(max_length=256, help_text='enter a valid github profile')
    review_text=models.TextField(help_text='enter your helpful review')

    def __str__(self):
        return 'review by '+self.name





            






    





