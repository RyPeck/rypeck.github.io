AUTHOR = "Ryan John Peck"
SITEURL = "http://rypeck.com"
SITENAME = "RyPeck Blog"
LOCALE = 'en_US.utf8'
TIMEZONE = 'America/New York'

DISPLAY_PAGES_ON_MENU = True
WITH_PAGINATION = True
DEFAULT_PAGINATION = 7
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

TWITTER_USERNAME = "rypeck"
GITHUB_URL = "https://github.com/rypeck"

SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/ryanjpeck"),
    ("GitHub", "https://github.com/ryanjpeck"),
    ("Twitter", "http://twitter.com/rypeck"),
)

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
