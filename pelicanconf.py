#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys

BASE_DIR = os.path.dirname(__file__)

# Clone the official plugin repo to the `official_plugins` dir
# (https://github.com/getpelican/pelican-plugins)
sys.path.append(os.path.join(BASE_DIR, "official_plugins"))

import summary, assets

AUTHOR = u'Leonardo Zhou'
SITENAME = u'\u7ffc\u56fe\u5357'
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    ('Python.org', 'http://python.org/'),
)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/glasslion'),
    ('github', 'https://github.com/glasslion'),
    ('google-plus', 'https://google.com/+LeonardoZhou'),
    ('envelope', 'mailto:glasslion@gmail.com'),
    ('stack-overflow', 'http://stackoverflow.com/users/1093020/leonardo-z'),
)

PLUGINS = [summary, assets]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Static content
STATIC_PATHS = ['images', 'extra/CNAME',]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Url
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Custom theme
THEME = '../pelican-themes/mnmlist'

QINIU_BUCKET_URL = 'http://wing2south.qiniudn.com'
