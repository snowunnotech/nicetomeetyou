from split_settings.tools import optional, include

include(
    'settings/base.py',
    optional('settings/local_settings.py'),
)