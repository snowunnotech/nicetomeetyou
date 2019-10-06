def setup_django_env():
    import os
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news.settings")
    django.setup()


def check_db_connection():
    from django.db import connection

    if connection.connection:
        if not connection.is_usable():
            connection.close()
