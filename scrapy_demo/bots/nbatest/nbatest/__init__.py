def setup_django_env():
    import sys, os, django
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('.'))))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'scrapy_demo.settings'
    django.setup()

def check_db_connection():
    from django.db import connection

    if connection.connection:
        if not connection.is_usable():
            connection.close()