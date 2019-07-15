#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from updata_data_to_sqlite import update_data_to_sqlite


def main():
    # do update data here change to cronjob better
    # update_data_to_sqlite()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Web_NBA.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
