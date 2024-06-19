import pymysql
import openpyxl

from config.DatabaseConfig import *

#학습 데이터 초기화
# 학습 데이터 초기화
def all_clear_train_data(db):
    # 기존 학습 데이터 삭제
    sql = '''
            delete from LB_chatbot_train_data
        '''
    with db.cursor() as cursor:
        cursor.execute(sql)

    # auto increment 초기화
    # sql = '''
    # ALTER TABLE LB_chatbot_train_data AUTO_INCREMENT=1
    # '''
    # with db.cursor() as cursor:
    #     cursor.execute(sql)


def insert_data(db, xls_row):
    print("xxxx   ",xls_row)

    intent, ner, query, answer, answer_url = xls_row

    sql = '''
            INSERT LB_chatbot_train_data(intent, query, answer, answer_url) 
            values(
             '%s', '%s', '%s', '%s'
            )
        ''' % (intent.value, query.value, answer.value, answer_url.value)

    sql = sql.replace("'None'", "null")
    #엑셀에서 불러온 cell에 데이터가 없는 경우, null로 치환
    with db.cursor() as cursor:
        cursor.execute(sql)
        print('{} 저장'.format(query.value))
        db.commit()


train_file = 'C:\\Users\\wmk51\\PycharmProjects\\LB_project\\train_tools\\qna\\train_data .xlsx'

db=None

try:
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

    #기존 학습 데이터 초기화
    all_clear_train_data(db)

    #학습 엑셀 파일 불러오기
    wb = openpyxl.load_workbook(train_file)
    sheet = wb['Sheet1']
    for row in sheet.iter_rows(min_row=2):
        insert_data(db, row)
    wb.close()

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()


