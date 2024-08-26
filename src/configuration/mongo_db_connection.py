import os
import sys

import certifi
import pymongo

from src.constant import *
from src.exception import CustomException

ca = certifi.where()

class MongoDBClinent:

    def __init__(self,database_name = MONGO_DATABASE_NAME) -> None: # type: ignore
        try:
            if MongoDBClinent.client is None:
                mongo_db_url = os.getenv("MOONGO_DB_URL")
                if mongo_db_url is None:
                    raise Exception("Environment key: MONGO_DB_URL is not set.")
                MongoDBClinent.client =pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
            self.client =MongoDBClinent.client
            self.database =self.client[database_name]
            self.database_name = database_name
        except Exception as o:
            raise CustomException(o, sys)

