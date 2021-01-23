"""Main configuration file.

Note:
    Credentials and environment variables are being pulled through the
    platform.sh configuration.
"""
from platformshconfig import Config


# Branding and customization options
BRAND = "VaccinateX"
TITLE = "VaccinateX"
LOGO = "default_logo.svg"
COPYRIGHT = "Helpful Engineering"
DESCRIPTION = "Collaborative effort to map available vaccine doses."
TERMSOFUSE = "http://okfn.org/terms-of-use/"
DATAUSE = "http://opendatacommons.org/licenses/by/"
CONTACT_EMAIL = "info@helpfulengineering.org"
CONTACT_TWITTER = "helpfuleng"
APPS_PER_PAGE = 1

# Configuration object containing all the
# environment variables and credentials.
config = Config()

# Web server bind address and port, automatically
# mapped by the platform.sh router to the outside world.
# worker instances don't have a port attribute, so we
# need to fake it.
try:
    port = int(config.port)
except AttributeError:
    port = 0

HOST, PORT = "127.0.0.1", port

# PostgreSQL database connection string (data source name)
# including both the credentials and the server address.
SQLALCHEMY_DATABASE_URI = config.formatted_credentials(
    "database", "postgresql_dsn"
)

# Redis cache configuration without Sentinel support.
# This requires the no-sentinel branch of the PyBossa
# repository in order to work.
REDIS_SENTINEL = []
REDIS_CACHE_ENABLED = True
REDIS_HOST = config.credentials("cache")["host"]
REDIS_PORT = config.credentials("cache")["port"]
REDIS_KEYPREFIX = "pybossa_cache"
REDIS_MASTER = "mymaster"
REDIS_DB = 0

# Session secrets, automatically derived from the default
# platform.sh entropy, which is created during the
# first deployment and doesn't change over time.
ITSDANGEROUSKEY = config["PROJECT_ENTROPY"]
SECRET_KEY = config["PROJECT_ENTROPY"]
SECRET = config["PROJECT_ENTROPY"]

# File upload support, enabled for project thumbnails.
# You may need to provision more capacity in from
# .platform/services.yaml for other uses.
ALLOWED_EXTENSIONS = ["svg"]
UPLOAD_METHOD = "local"
UPLOAD_FOLDER = "uploads"

# The enforced privacy mode disables the user pages like statistics,
# leaderboard and top users for everybody but administrators.
ENFORCE_PRIVACY = True

# Debug mode, disabled in production.
DEBUG = False

# Mail setup
MAIL_SERVER = config["SMTP_HOST"]
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_PORT = 465
MAIL_DEFAULT_SENDER = "Helpful Engineering <info@helpfulengineering.org>"


# FIXME
# All these options should be documented and set to sensible defaults.
# Also, we should probably add the Airtable credentials here for the importer.
#
#
#                              ___, ____--'
#                         _,-.'_,-'      (
#                      ,-' _.-''....____(
#            ,))_     /  ,'\ `'-.     (          /\
#    __ ,+..a`  \(_   ) /   \    `'-..(         /  \
#    )`-;...,_   \(_ ) /     \  ('''    ;'^^`\ <./\.>
#        ,_   )   |( )/   ,./^``_..._  < /^^\ \_.))
#       `=;; (    (/_')-- -'^^`      ^^-.`_.-` >-'
#       `=\\ (                             _,./
#         ,\`(   HIC  SVNT  DRACONES   )^^^
#           ``;         __-'^^\       /
#             / _>emj^^^   `\..`-.    ``'.
#            / /               / /``'`; /
#           / /          ,-=='-`=-'  / /
#     ,-=='-`=-.               ,-=='-`=-.
#   *******************************************


TWITTER_CONSUMER_KEY=config["TWITTER_CONSUMER_KEY"]
TWITTER_CONSUMER_SECRET=config["TWITTER_CONSUMER_SECRET"]
FACEBOOK_APP_ID=config["FACEBOOK_APP_ID"]
FACEBOOK_APP_SECRET=config["FACEBOOK_APP_SECRET"]
GOOGLE_CLIENT_ID=config["GOOGLE_CLIENT_ID"]
GOOGLE_CLIENT_SECRET=config["GOOGLE_CLIENT_SECRET"]

## Supported Languages
## NOTE: You need to create a symbolic link to the translations folder, otherwise
## this wont work.
## ln -s pybossa/themes/your-theme/translations pybossa/translations
#DEFAULT_LOCALE = "en"
#LOCALES = [("en", "English"), ("es", u"Español"),
#           ("it", "Italiano"), ("fr", u"Français"),
#           ("ja", u"日本語"),("pt_BR","Brazilian Portuguese")]


## list of administrator emails to which error emails get sent
# ADMINS = ["me@sysadmin.org"]

## CKAN URL for API calls
#CKAN_NAME = "Demo CKAN server"
#CKAN_URL = "http://demo.ckan.org"


## logging config
# Sentry configuration
# SENTRY_DSN=""
## set path to enable
# LOG_FILE = "/path/to/log/file"
## Optional log level
# import logging
# LOG_LEVEL = logging.DEBUG



## Announcement messages
## Use any combination of the next type of messages: root, user, and app owners
## ANNOUNCEMENT = {"admin": "Root Message", "user": "User Message", "owner": "Owner Message"}



## If you want to use Rackspace for uploads, configure it here
# RACKSPACE_USERNAME = "username"
# RACKSPACE_API_KEY = "apikey"
# RACKSPACE_REGION = "ORD"

## Default number of users shown in the leaderboard
# LEADERBOARD = 20
## Default shown presenters
# PRESENTERS = ["basic", "image", "sound", "video", "map", "pdf"]
# Default Google Docs spreadsheet template tasks URLs
TEMPLATE_TASKS = {
    "image": "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdHFEN29mZUF0czJWMUhIejF6dWZXdkE&usp=sharing",
    "sound": "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdEczcWduOXRUb1JUc1VGMmJtc2xXaXc&usp=sharing",
    "video": "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdGZ2UGhxSTJjQl9YNVhfUVhGRUdoRWc&usp=sharing",
    "map": "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdGZnbjdwcnhKRVNlN1dGXy0tTnNWWXc&usp=sharing",
    "pdf": "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdEVVamc0R0hrcjlGdXRaUXlqRXlJMEE&usp=sharing"}

# Expiration time for password protected project cookies
PASSWD_COOKIE_TIMEOUT = 60 * 30

# Expiration time for account confirmation / password recovery links
ACCOUNT_LINK_EXPIRATION = 5 * 60 * 60

## Ratelimit configuration
# LIMIT = 300
# PER = 15 * 60

# Disable new account confirmation (via email)
ACCOUNT_CONFIRMATION_DISABLED = True

# Mailchimp API key
# MAILCHIMP_API_KEY = "your-key"
# MAILCHIMP_LIST_ID = "your-list-ID"

# Flickr API key and secret
# FLICKR_API_KEY = "your-key"
# FLICKR_SHARED_SECRET = "your-secret"

# Dropbox app key
# DROPBOX_APP_KEY = "your-key"

# Send emails weekly update every
# WEEKLY_UPDATE_STATS = "Sunday"

# Youtube API server key
# YOUTUBE_API_SERVER_KEY = "your-key"

# Healthsite API key
HEALTHSITES_API_KEY=config["HEALTHSITES_API_KEY"]

# Enable Server Sent Events
# WARNING: this will require to run PyBossa in async mode. Check the docs.
# WARNING: if you don"t enable async when serving PyBossa, the server will lock
# WARNING: and it will not work. For this reason, it"s disabled by default.
# SSE = False

# Add here any other ATOM feed that you want to get notified.
NEWS_URL = ["https://github.com/pybossa/enki/releases.atom",
            "https://github.com/pybossa/pybossa-client/releases.atom",
            "https://github.com/pybossa/pbs/releases.atom"]

# Pro user features. False will make the feature available to all regular users,
# while True will make it available only to pro users
PRO_FEATURES = {
    "auditlog":              True,
    "webhooks":              True,
    "updated_exports":       True,
    "notify_blog_updates":   True,
    "project_weekly_report": True,
    "autoimporter":          True,
    "better_stats":          True
}

# Libsass style. You can use nested, expanded, compact and compressed
LIBSASS_STYLE = "compressed"

# CORS resources configuration.
# WARNING: Only modify this if you know what you are doing. The below config
# are the defaults, allowing PYBOSSA to have full CORS api.
# For more options, check the Flask-Cors documentation: https://flask-cors.readthedocs.io/en/latest/
# CORS_RESOURCES = {r"/api/*": {"origins": "*",
#                               "allow_headers": ["Content-Type",
#                                                 "Authorization"],
#                               "methods": "*"
#                               }}

# Email notifications for background jobs.
# FAILED_JOBS_MAILS = 7
# FAILED_JOBS_RETRIES = 3

# Language to use stems, full text search, etc. from postgresql.
# FULLTEXTSEARCH_LANGUAGE = "english"
