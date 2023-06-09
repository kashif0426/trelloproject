from django.db import models

class Task(models.Model):
    title = models.CharField(max_length= 250)
    what_to_do = models.TextField(blank = True, null= True)
    when_to_do = models.DateField(blank= True, null= True)
    do_status = models.BooleanField(default= True)
    working_status = models.BooleanField(default= False)
    done_status = models.BooleanField(default= False)
    
    def __str__ (self):
        return self.title
