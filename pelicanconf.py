AUTHOR = 'SlashGordon'
SITENAME = 'portfolioplus'
SITEURL = ''
MAIN_MENU = True
PATH = "content"

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)


from mysiteplugins import stocks
import os

PLUGINS = [stocks, "pelican.plugins.webassets"]
DEFAULT_PAGINATION = 10

STATIC_PATHS = ["dist"]
THEME ="themes/stocks"
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = os.environ.get("DEBUG", "0") == "1"