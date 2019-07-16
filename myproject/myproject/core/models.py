from django.db import models

class InformationBase(models.Model):
    create_datetime = models.DateTimeField(auto_now_add=True, null=True)
    update_datetime = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class New(InformationBase):
    url = models.CharField(max_length=128, unique=True)
    title_image_url = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.title
