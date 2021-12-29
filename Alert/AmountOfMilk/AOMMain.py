#乳量低下アラートの実行ファイル

# 設定ファイルを読み込む処理
import sys, os, pathlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from notifyAOM import notifyAOM #スラックを送るクラス
from getSetting import getSetting   #設定ファイルのクラス
from GetLowMilkCow import getLowAOMCow
from DirectoryOperator import DirectoryOperator
SET = getSetting().getSettingFile()


# 実行する処理
def main():
    SLACK_API = SET["slackAPI"]
    USER_NAME = SET["AOM"]["userName"]
    ICON_EMOJI = SET["AOM"]["iconEmoji"]
    LIMIT = SET["AOM"]["limit"]
    FILE_PATH = pathlib.Path(SET["dirPath"]["AOM"])
    FILE_LIMITS = SET["fileLimits"]

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    DirOpe = DirectoryOperator(FILE_PATH)
    DirOpe.deleteOldFiles(FILE_LIMITS)

    target_path = DirOpe.findRecentFile()
    Messenger = notifyAOM(SLACK_API, USER_NAME, ICON_EMOJI)
    AOM_df = getLowAOMCow(target_path, LIMIT)
    Messenger.createMessage(AOM_df, LIMIT)

main()