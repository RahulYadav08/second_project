from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='images/th.jpg')


    class Meta:
        verbose_name_plural = "Member's"
    def __str__(self):
        return self.name
    
class Relationship(models.Model):
    relationship_choices = (
        ('Mother', 'mother'),
        ('Father', 'father'),
        ('Husband', 'husband'),
        ('Wife', 'wife'),
        ('Son', 'son'),
        ('DaughterInLaw', 'daughterinlaw'),
        ('Brother', 'brother'),
        ('SisterInLaw', 'sisterinlaw'),
    )
    from_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='from_relationship')
    to_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='to_relationship')
    relationship_type = models.CharField(max_length=25,choices=relationship_choices)
    def __str__(self):
        return f"{self.from_member} -> {self.relationship_type} -> {self.to_member}"
    
