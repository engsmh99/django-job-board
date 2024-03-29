from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),

)

class job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=50,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Category(models.Model): 
    name = models.CharField(max_length=25)

    def __str__(self): 
        return self.name