AUTHOR = 'FuRong'
SITENAME = 'Programmering B'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    #("You can add links in your config file", "#"),
    #("Another social link", "#"),
)
DISPLAY_CATEGORIES_ON_MENU = True
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
        },
        'markdown.extensions.admonition': {},
        'markdown.extensions.extra': {
        },
        # optionally, more extensions,
        # e.g. markdown.extensions.meta
        'markdown.extensions.meta': {},
        'smarty' : {
            'smart_angled_quotes' : 'true'
        },
#        'markdown.extensions.toc': {
#            'permalink': 'true',
#        },
    },
#    'output_format': 'html5',
}

DEFAULT_PAGINATION = 10


THEME = "/home/rf/Documents/pelican-themes/bootstrap2"

#THEME = "notmyidea"
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['pictures']
