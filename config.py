import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Forms configuration
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# Supported OpenID providers list
OPENID_PROVIDERS = [
        { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
        { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
        { 'name': 'AOL', 'url': 'https://openid.aol.com/<username>' },
        { 'name': 'Flickr', 'url': 'https://www.flickr.com/<username>' }, ]

# Migration management
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
