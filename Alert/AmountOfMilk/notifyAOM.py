#乳量低下アラートを送信するクラス

# 設定ファイルを読み込む処理
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SendSlack import SendSlack

#クラス本文
class notifyAOM(SendSlack):
    def __init__(self, slack_api_url, user_name, icon_emoji):
        super().__init__(slack_api_url, user_name, icon_emoji)


    def createMessage(self, df, limits):
        #乳量低下牛データフレームからスラックに送るメッセージを作成する
        from datetime import date
        message = f'{date.today()}のレポート \n' 

        if len(df) == 0:
            message += '本日の乳量低下アラートはありません。'
            print(message)
            # super().send2Slack(message)
            return 
        message += f'乳量が{limits}%以上低下した牛が{len(df)}頭いました。\n'
        for i in range(len(df)):
            COWNUM = df.iloc[i, 0]          #牛番号
            TODAYAOM = df.iloc[i, 1]        #昨日の乳量
            YESTERDAYAOM = df.iloc[i, 2]    #一昨日の乳量
            RATEOFDECLINE = 100 - df.iloc[i, 3]   #乳量減少率

            message += f'・{COWNUM}番；{RATEOFDECLINE}%低下 ' \
                    f'(2日前: {YESTERDAYAOM}kg -> 1日前: {TODAYAOM}kg) \n'
        message = message[:-2]
        print(message)
        # super().send2Slack(message)