from django.db import models

# Create your models here.

class flip(models.Model):
    description=models.CharField(max_length=500)
    orientation=models.CharField(
                max_length=200,
                choices=[
                        ('protrait', 'Portrait'),
                        ('landscape', 'Landscape')
                        ],
                default='portrait',
                )
