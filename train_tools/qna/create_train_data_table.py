# import pymysql
# from config.DatabaseConfig import *
#
# db = None
# try:
#     db = pymysql.connect(host=DB_HOST,
#                          user=DB_USER,
#                          passwd=DB_PASSWORD,
#                          db=DB_NAME,
#                          charset='utf8')
#
#     sql = '''
#         CREATE TABLE IF NOT EXISTS `LB_chatbot_train_data` (
#         `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
#         `intent` VARCHAR(200) NULL,
#         `query` TEXT NULL,
#         `models` VARCHAR(100) NULL,
#         `answer` TEXT NOT NULL,
#         PRIMARY KEY (`id`)
#         ) ENGINE=InnoDB DEFAULT CHARSET=utf8
#     '''
#
#     # 테이블 생성
#     with db.cursor() as cursor:
#         cursor.execute(sql)
#         db.commit()
#
# except Exception as e:
#     print(e)
# finally:
#     if db is not None:
#         db.close()
import pymysql
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from config.DatabaseConfig import *



db = None
try:
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

    # 테이블 생성 sql 정의
    sql = '''
      CREATE TABLE IF NOT EXISTS `LB_chatbot_train_data` (
      `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
      `intent` VARCHAR(45) NULL,
      `query` TEXT NULL,
      `answer` TEXT NOT NULL,
      `answer_url` TEXT NULL,
      PRIMARY KEY (`id`))
    ENGINE = InnoDB DEFAULT CHARSET=utf8
    '''

    # 테이블 생성
    with db.cursor() as cursor:
        cursor.execute(sql)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()