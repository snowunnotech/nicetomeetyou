from django.core.management.base import BaseCommand, CommandError
from ._crawl import crawl


class Command(BaseCommand):
    help = 'This customized command is for scheduling the crawling task'

    def handle(self, *args, **options):
        try:
            crawl()
        except CommandError:
            raise CommandError('Crawling Task Failed')
