from django.db import models

# Create your models here.

Job_Type = ( 
    ('Full-Time','24h-Time'),
    ('Part-Time','9h-Time')
     )

class Job(models.Model): # table
    Title = models.CharField(max_length = 100) # column
    #Location = 
    job_Type = models.CharField(max_length = 20,choices = Job_Type)
    Description = models.TextField(max_length = 1000 )
    Published_at = models.DataTimeField(auto_now = True)
    Vacancy = models.IntegerField(default = 1) 
    Salary = models.IntegerField(default = 0)
    Experience = models.IntegerField(default = 1)

    def __str__(self):
        return self.Title
    