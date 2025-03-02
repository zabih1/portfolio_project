from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    logo_image = models.ImageField(upload_to='logo_images/', blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    bio = models.TextField()
    short_bio = models.TextField(blank=True, help_text="A short version of your bio for the homepage")
    experience_years = models.IntegerField(default=0)
    cv_file = models.FileField(upload_to='cv_files/', blank=True, null=True)
    intro_video = models.FileField(upload_to='videos/', blank=True, null=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    
    # New dynamic field for top skills
    top_skills = models.ManyToManyField('Skill', related_name='profiles', blank=True)

    def __str__(self):
        return self.name



class Skill(models.Model):
    SKILL_TYPES = [
        ('technical', 'Technical Skill'),
        ('professional', 'Professional Skill'),
    ]
    
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Proficiency percentage (0-100)")
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPES)
    
    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Technologies"

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    time_period = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0, help_text="Order to display (lower numbers shown first)")
    
    def __str__(self):
        return self.degree
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Education"

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    time_period = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0, help_text="Order to display (lower numbers shown first)")
    
    def __str__(self):
        return self.position
    
    class Meta:
        ordering = ['order']

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    demo_url = models.URLField(blank=True)
    source_code_url = models.URLField(blank=True)
    technologies = models.ManyToManyField(Technology)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name}: {self.subject}"