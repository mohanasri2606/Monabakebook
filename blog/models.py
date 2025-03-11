from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Category
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self) :
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField(default="")  
    ingredients = models.TextField(default="")  
    recipe = models.TextField(default="") 
    tips = models.TextField(default="")  
    img = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField()
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) :
        return self.title
    

class AboutUs(models.Model):
    content = models.TextField()

    

