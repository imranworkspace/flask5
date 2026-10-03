from dotenv import load_dotenv
import os 

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ENGINE_OPTIONS={
        'pool_size':10,
        'max_overflow':5,
        'pool_pre_config':True
    }