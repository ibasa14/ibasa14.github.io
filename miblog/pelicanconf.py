#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Ignacio basagoiti'
SITENAME = 'Artículos por Ignacio Basagoiti'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)



DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME='pelican-clean-blog-master'

HEADER_COVER = 'images/indexheader.jpg'
HEADER_COLOR = 'black'
SOCIAL = (('github', 'https://github.com/ibasa14'),)
COLOR_SCHEME_CSS = 'github.css'
#CSS_OVERRIDE = 'clean-blog.min.css'
STATIC_PATHS = ['images','extra/ib_favicon.ico']
FOOTER_INCLUDE = 'my_footer.html'
IGNORE_FILES = [FOOTER_INCLUDE,".ipynb_checkpoints"]
THEME_TEMPLATES_OVERRIDES = [PATH]
#SHOW_SOCIAL_ON_INDEX_PAGE_HEADER=True
LOAD_CONTENT_CACHE = False
PLUGIN_PATHS = [PATH]
PLUGINS = ['sitemap', 'pelican-ipynb.markup']
MARKUP = ('md', 'ipynb')
FAVICON = 'ib_favicon.ico'
EXTRA_PATH_METADATA = {
    'extra/ib_favicon.ico': {'path': 'ib_favicon.ico'}
}