import threading
import json

from config.DatabaseConfig import *
from utils.Database import Database
from utils.BotServer import BotServer
from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel
from utils.FindAnswer import FindAnswer


p = Preprocess(word2index_dic='train_tools/dict/chatbot_dict.bin',
               userdic='C:\\Users\\wmk51\\PycharmProjects\\LB_project\\utils\\user_dict.tsv')
#의도 파악 모듈
intent = IntentModel(model_name='models/intent/intent_model.h5',proprecess=p)

def to_client(conn, addr, params):
    db = params['db']

    try:
        db.connect() #DB 연결

        #데이터 수신
        read = conn.recv(2048)
        print("="*60)
        print(f"Connection from {addr}")

        if read is None or not read:
            #클라이언트 연결이 끊어지거나, 오류가 있는 경우
            print("클라이언트 연결 끊어짐")
            exit(0)

        # 수신된 데이터를 json 형식으로 변환
        recv_json_data = json.loads(read.decode())
        print("데이터 수신 : ", recv_json_data)
        query = recv_json_data['Query']

        #의도 파악
        intent_predict = intent.predict_class(query)
        intent_name = intent.labels[intent_predict]

        #답변 검색
        try:
            f = FindAnswer(db)
            answer_og = f.search(intent_name)
            answer = answer_og[0]
            answer_url = answer_og[1]



        except Exception as e:
            answer = "죄송해요 무슨 말인지 모르겠어요"

        send_json_data_str = {
            "Query": query,
            "Answer": answer,
            "Intent": intent_name,
            "Answer_url" : answer_url
        }

        message = json.dumps(send_json_data_str)
        conn.send(message.encode())

    except Exception as ex:
        print(ex)
    finally:
        if db is not None:
            db.close()
        conn.close()
if __name__ == '__main__':
    #질문/답변 학습 DB 연결 객체 생성
    db = Database(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db_name=DB_NAME
    )
    print("DB 접속")

    port = 5050
    listen = 100

    #봇 서버 동작
    bot = BotServer(port, listen)
    bot.create_sock()
    print("bot start")

    while True:
        conn, addr = bot.ready_for_client()
        params = {
            'db': db
        }

        client = threading.Thread(target=to_client, args=(conn, addr, params))
        client.start()