from flask import Flask
# from flask_mongoalchemy import MongoAlchemy
from flask_mongoengine import MongoEngine
import logging
from config import Config
# from config import Config

# db = MongoAlchemy()
db = MongoEngine()

# class Config:
#     DEBUG = True
#     app = Flask(__name__)
#     # app.config['MONGODB_SETTINGS'] = {
#     #     "db": "company",
#     # }
#     # MONGO_URI = "mongodb://localhost:27017/company"
#     # app.config['MONGOALCHEMY_DATABASE'] = 'company'
#     # app.config["MONGODB_HOST"] = MONGO_URI
#     # db = MongoAlchemy()


#     # MONGOALCHEMY_DATABASE = 'company'


#     app.config['MONGODB_SETTINGS'] = {
#         'db': 'company',
#         'host': 'localhost',
#         'port': 27017
#     }

def create_app():
    try:
        print("---------------------------1")
        app = Flask(__name__)
        # app.config["MONGO_URI"] = "mongodb://localhost:27017/company"
        
        app.config.from_object(Config)
        print("-------------2")

        db.init_app(app)
        print("-------------3")
        from .views import users_bp
        app.register_blueprint(users_bp)
        print("-------------4")

        return app

    except Exception as ex:
        print("**************")
        logging.error(ex)
        print("*********************")
