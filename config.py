from os import path, getenv
basedir = path.abspath(path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "this-really-needs-to-be-changed"
    SQLALCHEMY_DATABASE_URI = "postgresql://higiewpngvycli:6a67fb53f9671eb61d86ec0c6bfb5768675608eec30b4cda4e45da330226ead0@ec2-54-217-222-254.eu-west-1.compute.amazonaws.com:5432/d1fgh5p36f478d"
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