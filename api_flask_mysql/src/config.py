from decouple import config

class config:
    SECRET_KEY =config('SECRET_KEY')
class DevelopmentConfig():
    DEBUG=True
    # MYSQL_USER ='root'
    # MYSQL_PASSWORD='admin'
    # MYSQL_DB = 'api_flask'
    
config = {
    'development': DevelopmentConfig,
}