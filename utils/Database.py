import pymysql
import pymysql.cursors
import logging


class Database:
    '''
        데이터 베이스 제어
    '''

    def __init__(self,host,user,password,db_name,charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.db_name = db_name
        self.conn = None

    #DB 연결
    def connect(self):
        if self.conn != None:
            return

        self.conn = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    db=self.db_name,
                                    charset=self.charset
                                    )

    def close(self):
        if self.conn != None:
            return
        if not self.conn.open:
            return
        self.conn.close()
        self.conn = None

    def execute(self,sql):
        last_row_id = -1
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
            self.conn.commit()
            last_row_id = cursor.lastrowid
        except Exception as ex:
            logging.error(ex)
        finally:
            return last_row_id

    #select 구문에서 단 1개의 데이터 row만 불러온다
    def select_one(self,sql):
        result = None

        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        except Exception as ex:
            logging.error(ex)

        finally:
            return result

    #select 구문 실행 후, 전체 데이터 ROW만 불러옴
    def select_all(self,sql):
        result = None

        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
        except Exception as ex:
            logging.error(ex)
        finally:
            return result
        