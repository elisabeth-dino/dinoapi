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

    SQLALCHEMY_DATABASE_URI = "postgres://nqwcwvxisqsacq:6081c0b76fbec03b9d61c87f43ce7c65f68977fd786c5aac8348397d55a98704@ec2-54-163-234-88.compute-1.amazonaws.com:5432/d8a5amvsvl46d8"