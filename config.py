import os

class Config:
    
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://clara:qwerty@localhost/pitch'
    SECRET_KEY='098765'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mary.auma@student.moringaschool.com' 
    MAIL_PASSWORD = '0716478973'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://clara:qwerty@localhost/pitch'
    

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}