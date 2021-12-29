class SendSlack() :
    def __init__(self, slack_api_url, user_name, icon_emoji):
        self.slack_api_url = slack_api_url
        self.user_name = user_name
        self.icon_emoji = icon_emoji

    def send2Slack(self, message):
        #メッセージをスラックに投げるメソッド
        import requests, json, time
        payload = {
            'text': message,  #通知内容
            'username': self.user_name,  #ユーザー名
            'icon_emoji': self.icon_emoji,  #アイコン
        }
        for i in range(18):     #通信が悪い場合の処理: 3時間ほど繰り返す
            try :
                requests.post(self.slack_api_url, data = json.dumps(payload))
            except:
                time.sleep(600)
            else :
                break

