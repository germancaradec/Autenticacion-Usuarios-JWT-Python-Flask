from decouple import config
from src.utils.errors.CustomException import CustomException
import pymysql


def get_connection():
    try:
        return pymysql.connect(
            host=config('MYSQL_HOST'),
            user=config('MYSQL_USER'),
            password=config('MYSQL_PASSWORD'),
            db=config('MYSQL_DB'),
            port=int(config('MYSQL_PORT'))
        )
    except CustomException as ex:
        raise CustomException(ex)
