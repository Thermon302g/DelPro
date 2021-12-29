# カウトラップが適用されている牛を探すプログラム

# 設定ファイルを読み込む処理
import sys, os

from pandas.core.algorithms import diff
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from getSetting import getSetting
SET = getSetting().getSettingFile()

# スクリプト本文
def getTrappedCow(file_path) -> object:
    #乳量がrate_of_decline%低下した牛をピックアップするメソッド
    import pandas as pd
    ENCODING = SET['AOM']['encoding']
    TRAPPED = SET["CowTrap"]["trapped"]
    UNTRAPPED = SET["CowTrap"]["untrapped"]

    df = pd.read_csv(file_path, encoding=ENCODING)
    df = df[df[TRAPPED] != UNTRAPPED]
    return df

if __name__ == '__main__':
    #テストコード
    df = getTrappedCow("/Users/natsukiishikura/Documents/DP_Project/Alerts/CowTrap/CowTrap_20211218 120000.csv")
    print(df)