#カウトラップ監視システムの実行ファイル

# 設定ファイルを読み込む処理
import sys, os, pathlib
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from notifyTrappedCow import notifyTrappedCow #スラックを送るクラス
from getSetting import getSetting   #設定ファイルのクラス
from GetTrappedCow import getTrappedCow
from DirectoryOperator import DirectoryOperator
SET = getSetting().getSettingFile()


# 実行する処理
def main():
    SLACK_API = SET["slackAPI"]
    USER_NAME = SET["CowTrap"]["userName"]
    ICON_EMOJI = SET["CowTrap"]["iconEmoji"]
    FILE_PATH = pathlib.Path(SET["dirPath"]["CowTrap"])
    FILE_LIMITS = SET["fileLimits"]

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    DirOpe = DirectoryOperator(FILE_PATH)
    DirOpe.deleteOldFiles(FILE_LIMITS)

    target_path = DirOpe.findRecentFile()
    Messenger = notifyTrappedCow(SLACK_API, USER_NAME, ICON_EMOJI)
    trapped_df = getTrappedCow(target_path)
    Messenger.createMessage(trapped_df)

main()