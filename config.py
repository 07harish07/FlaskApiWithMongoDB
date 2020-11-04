from flask import Flask
# class Config:
#     DEBUG = True
#     MONGOALCHEMY_DATABASE = 'company'

class Config:
    DEBUG = True
    app = Flask(__name__)
    # app.config['MONGODB_SETTINGS'] = {
    #     "db": "company",
    # }
    # MONGO_URI = "mongodb://localhost:27017/company"
    # app.config['MONGOALCHEMY_DATABASE'] = 'company'
    # app.config["MONGODB_HOST"] = MONGO_URI
    # db = MongoAlchemy()


    # MONGOALCHEMY_DATABASE = 'company'


    app.config['MONGODB_SETTINGS'] = {
        'db': 'company',
        'host': 'localhost',
        'port': 27017
    }