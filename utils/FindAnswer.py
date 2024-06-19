class FindAnswer:
    def __init__(self,db):
        self.db = db

    #검색 쿼리 생성
    def _make_query(self, intent_name):
        sql = "select * from LB_chatbot_train_data"
        if intent_name != None:
            sql = sql + " where intent='{}'".format(intent_name)

        sql = sql + " order by rand() limit 1"
        return sql

    def search(self, intent_name):
        #의도명과 개체명으로 답변 검색
        sql = self._make_query(intent_name)
        answer = self.db.select_one(sql)

        return (answer['answer'], answer['answer_url'])