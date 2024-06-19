from utils.Preprocess import Preprocess

sent = "내일 오전 10시에 대출 상담 예약해줘"

#전처리 객체 생성
p = Preprocess(userdic='C:\\Users\\wmk51\\PycharmProjects\\LB_project\\utils\\user_dict.tsv')

#형태소 분석기
pos = p.pos(sent)

#품사 태그와 같이 키워드 출력
ret = p.get_keywords(pos, without_tag=False)
print(ret)
#품사 태그 없이 키워드 출력
ret = p.get_keywords(pos, without_tag=True)
print(ret)