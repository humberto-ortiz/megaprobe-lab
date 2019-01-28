#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Humberto Ortiz-Zuazaga'
SITENAME = u'MegaProbe Lab'
SITELOGO = "images/k-logo-tiny.png"
SITELOGO_SIZE = 37
SITEURL = ''

TIMEZONE = 'America/Puerto_Rico'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('CCOM', 'http://ccom.uprrp.edu/'),
          ('HPCf', 'http://hpcf.upr.edu/'),
          ('UPR-RP', 'http://www.uprrp.edu/'),)


# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME="../pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_NAVBAR_INVERSE = True

# License
CC_LICENSE = "CC-BY-SA"

# Plugins, especially for IPython notebooks and mathjax
PLUGIN_PATHS = ["../pelican-plugins"]

## bootswatch-markdown applies table class to tables (much nicer)
PLUGINS = ["bootswatch_markdown_css", 'i18n_subsites']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

DISPLAY_PAGES_ON_MENU = True
