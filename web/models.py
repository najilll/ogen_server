from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    video = models.FileField(upload_to='banners/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Enquiry(models.Model):
    QUALIFICATION = (
        ('10th', '10th'),
        ('12th', '12th'),
        ('Diploma', 'Diploma'),
        ('Bachelors', 'Bachelors'),
        ('Masters', 'Masters'),
        ('Other', 'Other'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    mobilenumber = models.CharField(max_length=15)
    age = models.IntegerField()
    qualification = models.CharField(max_length=20, choices=QUALIFICATION)
    location = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry from {self.name} <{self.email}>"
    
class Offer_Section(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='offer_images/',help_text="Image size should be (340x1320")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Top_Destinations(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='destination_images/',help_text="Image size should be (312x312")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Courses(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='course_images/',help_text="Image size should be (648x385)")
    duration = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True,help_text="Course country/location")
    price = models.CharField(max_length=100, blank=True, null=True)
    about = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Faq(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=300)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonial_images/',help_text="Image size should be (55x55)")
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class SuccessStories(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='success_story_images/',help_text="Image size should be (370x370)")
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    is_home = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name