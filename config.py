import os

from flask import Config
class Config:

    NEWS_API_KEY= os.environ.get('NEWS_API_KEY')
    USE_BASE_URL = 'https://newsapi.org/v2/{}?q=00f0b05c0edb45a38a541d1d9bbcab6b'
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}