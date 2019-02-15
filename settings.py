import os

class DBSettings:
    #add db information
    DB_ENGINE = "postgresql"
    DB_HOST = os.getenv("RDS_HOSTNAME","127.0.0.1")
    DB_NAME = os.getenv("RDS_DB_NAME","testapi")
    DB_PORT = os.getenv("RDS_PORT","5432")
    DB_USER = os.getenv("RDS_USERNAME","postgres")
    DB_PASSWORD = os.getenv("RDS_PASSWORD","api")
    #SQLALCHEMY_DATABASE_URI = "{0}://{1}:{2}@{3}:{4}/{5}".format(DB_ENGINE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

    SQLALCHEMY_DATABASE_URI = "postgres://ldkflufqqnfpzi:1c8543600224f62a7bf23799860f681386c3af921df432930f0da6f419297063@ec2-50-17-193-83.compute-1.amazonaws.com:5432/d9qgvsgco4ml2l"