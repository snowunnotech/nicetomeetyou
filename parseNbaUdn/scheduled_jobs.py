import requests
from django_cron import CronJobBase, Schedule
from .models import TopNews
from .parser import TopNewsParser


class ParseNewNews(CronJobBase):
    RUN_EVERY_MINS = 5 # every 5 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'parseNbaUdn.scheduled_jobs'    # a unique code

    def do(self):
        # parse and save top newses' title, link, thumb img link
        index_url = 'https://nba.udn.com/nba/index?gr=www'
        base_url = 'https://nba.udn.com'
        page = requests.get(index_url)
        p = TopNewsParser()
        p.feed(page.text)
        # reversed saving (newest has newest id)
        for n in reversed(p.news_list):
            try:
                TopNews.objects.get(postId=n.postId)
            except TopNews.DoesNotExist:
                TopNews(postId=n.postId,
                        title=n.title,
                        imgUrl=n.imgUrl,
                        pageUrl=base_url + n.pageUrl
                        ).save()
            finally:
                pass
