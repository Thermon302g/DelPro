# 乳量を確認するプログラム

# 設定ファイルを読み込む処理
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from SendSlack import SendSlack
from getSetting import getSetting
SET = getSetting().getSettingFile()

# スクリプト本文
def getLowAOMCow(file_path, limits) -> object:
    #乳量がrate_of_decline%低下した牛をピックアップするメソッド
    import pandas as pd
    ENCODING = SET['AOM']['encoding']
    TODAYAOM = SET['AOM']['todayAOM']
    YESTERDAYAOM = SET['AOM']['yesterdayAOM']
    RATE_OF_DECLINE = SET['AOM']["rateOfDeclline"]

    df = pd.read_csv(file_path, encoding="UTF-8")
    df[RATE_OF_DECLINE] = round(df[TODAYAOM] / df[YESTERDAYAOM] * 100, 1)
    return df[df[RATE_OF_DECLINE] < limits]


if __name__ == '__main__':
    #テストコード
    df = getLowAOMCow("/Users/natsukiishikura/Desktop/farmnote_backup/MilkYield/MilkYieldReport_20211217 234500.csv", 50)
    print(df)