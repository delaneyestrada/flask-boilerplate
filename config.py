import os

class Config(object):
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True