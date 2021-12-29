# 設定ファイルを読み込むためのクラス
FILENAME = "Setting.json"

class getSetting():
    #設定ファイルを読み込むためのクラス
    @classmethod
    def getSettingFile(cls):
        import os, json
        dir_path = os.path.dirname(os.path.abspath(__file__))
        file_obj = open(os.path.join(dir_path, FILENAME), "r")
        json_obj = json.load(file_obj)
        return json_obj