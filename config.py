import os
# basedir is set as a relative path from any place we call it to this file
basedir = os.path.abspath(os.path.dirname(__file__))

# Below I create a classes with the configuration settings for all the stages of my product. Config is the default config, ProductionConfig for production, etc.
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # SEND_FILE_MAX_AGE_DEFAULT makes it so the browser doesn't store any of the CSS or HTML in a cache. It makes for easier development
    SEND_FILE_MAX_AGE_DEFAULT = 0
    # EMAIL SETTINGs
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True # Config for XML sitemap
    # Mongoengine
    MONGODB_DB = 'portfolio-website'
    # MONGODB_HOST = 'mongodb://localhost/portfolio-website'
    MONGODB_HOST = os.environ['MONGODB_HOST']
    MONGODB_PORT = 27017
    # file upload 
    UPLOAD_FOLDER = './static/resume/'
    BLOG_FOLDER = './static/blog/'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


class ProductionConfig(Config):
    DEBUG = False
    # Allow flask-mail
    MAIL_SUPPRESS_SEND = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    # Suppress Flask Mail
    MAIL_SUPPRESS_SEND = False


class TestingConfig(Config):
    TESTING = True



