from app.extentions import db,migrate 
from dotenv import load_dotenv
import os 
from flask import Flask
from app.routers.stud_router import student_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("DATABASE_URL")
    # print(app.config.get('SQLALCHEMY_DATABASE_URI'))

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(
        student_bp,
        url_prefix="/api"
    )

    return app 