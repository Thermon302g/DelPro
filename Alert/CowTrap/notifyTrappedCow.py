#カウトラップ監視システムの通知を送信するクラス

# 設定ファイルを読み込む処理
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SendSlack import SendSlack

#クラス本文
class notifyTrappedCow(SendSlack):
    def __init__(self, slack_api_url, user_name, icon_emoji):
        super().__init__(slack_api_url, user_name, icon_emoji)


    def createMessage(self, df):
        #カウトラップフレームからスラックに送るメッセージを作成する
        from datetime import datetime
        dt_now = datetime.now()
        formatted_dt = dt_now.strftime('%Y-%m-%d %H:%M:%S')
        message = f'{formatted_dt}のカウトラップ設定状況 \n'
        if len(df) == 0:
            message += 'トラップされている牛はいません'
            print(message)
            # super().send2Slack(message)
            return 
        message += 'カウトラップが設定されています。\n'
        message += f'トラップされている牛は{len(df)}頭います。\n' 
        for i in range(len(df)):
            COWNUM = df.iloc[i, 0]          #牛番号
            message += f'   ・{COWNUM}番 \n'
        message = message[:-2]
        print(message)
        # super().send2Slack(message)



if __name__ == "__main__":
    from getSetting import getSetting
    from GetTrappedCow import getTrappedCow
    SET = getSetting.getSettingFile()
    SLACK_API = SET["slackAPI"]
    USER_NAME = SET["CowTrap"]["userName"]
    ICON_EMOJI = SET["CowTrap"]["iconEmoji"]
    file_path = "/Users/natsukiishikura/Documents/DP_Project/Alerts/CowTrap/CowTrap_20211218 120000.csv"
    NTC = notifyTrappedCow(SLACK_API, USER_NAME, ICON_EMOJI)
    df = getTrappedCow(file_path)
    NTC.createMessage(df)
