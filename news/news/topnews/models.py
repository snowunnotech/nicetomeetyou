from django.db import models

class News(models.Model):

    # Link to detail news on site: https://nba.udn.com/nba/news/
    link = models.URLField(max_length=100)

    # Preview image
    pre_img_link = models.URLField(max_length=100)

    # News title
    title = models.CharField(max_length=50)

    # News published time from now (Save as string)
    time = models.CharField(max_length=10)

    # Preview
    preview = models.CharField(max_length=100)

    # Image
    img_link = models.URLField(max_length=100)

    # Paragraph
    paragraph = models.CharField(max_length=200)

    # Crawl time
    crawl_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    