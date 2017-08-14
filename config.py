from os import path, getenv
basedir = path.abspath(path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "this-really-needs-to-be-changed"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1wal!col?33@localhost:5000/emerson_db"
    MAIL_USERNAME = getenv("MAIL_USERNAME", "florian.delvo@googlemail.com")
    MAIL_PASSWORD = getenv("MAIL_PASSWORD", "1wal!col?33")
    MAIL_DEFAULT_SENDER = getenv("MAIL_DEFAULT_SENDER", "Emerson Prime")
    MAIL_SERVER = getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(getenv("MAIL_PORT", "465"))
    MAIL_USE_SSL = int(getenv("MAIL_USE_SSL", True))
    USER_APP_NAME = "Emerson Prime"  # Used by email templates


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True