from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        verbose_name_plural = "Member's"
    def __str__(self):
        return self.name
    
