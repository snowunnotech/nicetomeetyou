from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class News(models.Model):

    title = models.CharField(max_length=100, verbose_name=_('標題'))
    content = models.TextField(verbose_name=_('內文'))
    created_at = models.DateTimeField(verbose_name=_('時間'))
    scrapped_at = models.DateTimeField(auto_now_add=True, verbose_name=_('抓取時間'))

    def __str__(self):
        return self.title

    # def __init__(self):
        # super(News, self).__init__()

    class Meta:
        verbose_name = _('新聞')
        verbose_name_plural = _('新聞列表')
