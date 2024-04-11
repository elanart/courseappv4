from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.
class User(AbstractUser):
    avatar = CloudinaryField(null=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=20, default='tag')

    def __str__(self):
        return self.name
    
    
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-id']
        
        
class Course(BaseModel):
    subject = models.CharField(max_length=255)
    description = RichTextField()
    image = CloudinaryField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.subject
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    
class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    image = CloudinaryField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    
    class Meta:
        unique_together = ('subject', 'course')
    
    def __str__(self):
        return self.subject
    
    
class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True
        
        
class Comment(Interaction):
    content = RichTextField()
    
    
class Like(Interaction):
    class Meta:
        unique_together = ('lesson', 'user')