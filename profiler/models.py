from django.db import models

# Create your models here.

class Profile(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    message = models.CharField(max_length=200)

    
    image = models.ImageField(blank=True, upload_to='shopping/')

class Projects(models.Model):
    def __str__(self):
        return self.name
    
    projects_name = models.CharField(max_length= 100)
    projects_explanation = models.CharField(max_length=5000)
    projects_language = models.CharField(max_length=10)
    projects_start = models.DateField()
    projects_end = models.DateField()
    projects_image = models.ImageField(blank=True, upload_to='profiler/')

class Resume(models.Model):
    def __str__(self):
        return self.resume_name
    
    resume_name = models.CharField(max_length=100)
    resume_experience_start = models.CharField(max_length=100)
    resume_experience_end = models.CharField(max_length=100)
    resume_experience_job = models.CharField(max_length= 100)
    resume_experience_company = models.CharField(max_length=200)
    resume_experience_location = models.CharField(max_length=200)
    resume_experience_explanation = models.TextField()
    
    resume_education_start = models.CharField(max_length=100)
    resume_education_end = models.CharField(max_length=100)
    resume_education_univ = models.CharField(max_length= 100)
    resume_education_univ_location= models.CharField(max_length=200)
    resume_education_major = models.CharField(max_length=200)
    resume_education_level = models.CharField(max_length=200)
    resume_education_explanation = models.TextField()
    
    
    resume_language = models.CharField(max_length=10)

    resume_professional_skills = models.CharField(max_length=30)


    resume_image = models.ImageField(blank=True, upload_to='profiler/')