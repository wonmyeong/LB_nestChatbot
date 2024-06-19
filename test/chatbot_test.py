from config.DatabaseConfig import *
from utils.Database import Database
from utils.Preprocess import Preprocess

#전처리 객체 생성
# 전처리 객체 생성
p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic='C:\\Users\\wmk51\\PycharmProjects\\LB_project\\utils\\user_dict.tsv')

#질문/답변 학습 DB 연결 객체 생성
db = Database(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    db_name=DB_NAME
)

db.connect()

#원문
query="주택 담보대출에 대해서 자세히 이야기 해줄래?"

#의도 파악
from models.intent.IntentModel import IntentModel
intent = IntentModel(model_name="../models/intent/intent_model.h5", proprecess=p)
predict = intent.predict_class(query)
intent_name = intent.labels[predict]

print("질문 : ", query)
print("=" * 100)
print("의도 파악 : ", intent_name)

from utils.FindAnswer import FindAnswer

try:
    f = FindAnswer(db)
    answer = f.search(intent_name)


except Exception as e:
    answer = "죄송해요 무슨 말인지 모르겠어요"

print("답변 : ",answer)
db.close()


