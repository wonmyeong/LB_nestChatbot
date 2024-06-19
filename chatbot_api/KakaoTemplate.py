class KakaoTemplate:
    def __init__(self):
        self.version = "2.0"

    def simpleTextComponent(selfself,text):
        return{
            "simpleText" : {"text" : text}

        }

    #사용자에게 응답 스킬 전송
    def send_response(self,bot_resp):
        responseBody = {
            "version": self.version,
            "template": {
                "outputs": []
            }
        }

        if bot_resp["Answer"] is not None:
            responseBody["template"]["outputs"].append(bot_resp["Answer"])


        return responseBody