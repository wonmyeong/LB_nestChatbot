import requests, json

# 보내기 API 인증키
authorization_key = 'BXaGYpMxSam7iVmmm3Pt'
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Authorization': authorization_key,
}

# 사용자 식별값, 보낼 메시지 정의
user_key = 1
data = {
    "event": "send",
    "user": user_key,
    "textContent": {"text": "hello world :D"}
}

# 보내기 API 호출
message = json.dumps(data) # JSON 문자열 변경
response = requests.post(
    'https://talk.naver.com/ct/w5uro1',
    headers=headers,
    data=message)
print(response.status_code)
print(response.text)