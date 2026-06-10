from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  # Mo ta

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True) #Tu them thoi gian

    def __str__(self):
        return self.title
class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/') 
    tech_stack = models.CharField(max_length=200) # VD: "Django, CSS, JS"
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
class Contact(models.Model):
    ho_ten = models.CharField(max_length=100)
    email = models.EmailField()
    tin_nhan = models.TextField()
    thoi_gian = models.DateTimeField(auto_now_add=True)
    sdt = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return f"{self.ho_ten} - {self.email}"
