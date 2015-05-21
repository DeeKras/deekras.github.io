#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dee Kras'
SITENAME = u'DeeKras.com'
SITEURL = 'www.deekras.com'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('github', 'deekras'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# THEME = "/home/deekras/pelican-themes/foundation-default-colours"
# THEME = "/home/deekras/pelican-themes/pelican-bootstrap3"
# THEME = "/home/deekras/pelican-themes/tuxlite_tbs"
# THEME = "/home/deekras/pelican-themes/blueidea"  -- pretty good choice
THEME = "/home/deekras/pelican-themes/built-texts"  

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
