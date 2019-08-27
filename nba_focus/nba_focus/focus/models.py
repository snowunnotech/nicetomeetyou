from django.db import models

class News(models.Model):
    """Model representing news."""
    title = models.CharField(primary_key=True, max_length=200, help_text='Enter a news title')
    url = models.TextField(max_length=1000, help_text='Enter a news url')
    time = models.CharField(null=True, blank=True, max_length=200, help_text='Enter a time')
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title}, {self.url}'
