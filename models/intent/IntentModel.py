import tensorflow as tf
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing

class IntentModel:
    def __init__(self, model_name, proprecess):

        #의도 클래스 별 레이블
        self.labels = {0:'주택담보대출', 1: '전세자금대출', 2:'신용대출', 3:'자동차대출'}
        self.model = load_model(model_name)
        self.p = proprecess

    def predict_class(self,query):

        #형태소 분석
        pos = self.p.pos(query)
        #문장 내 키워드 추출(불용어 제거)
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordidx_sequence(keywords)]

        # 단어 시퀀스 벡터 크기
        from config.GlobalParams import MAX_SEQ_LEN

        #패딩처리
        padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN,padding = 'post')
        predict = self.model.predict(padded_seqs)
        predict_class = tf.math.argmax(predict, axis=1)
        return predict_class.numpy()[0]
