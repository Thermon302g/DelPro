# ディレクトリ内のファイル数を整理する

class DirectoryOperator():
    #ディレクトリ操作を行うクラス
    def __init__(self, dir_path):
        self.dir_path = dir_path


    def findRecentFile(self):
        # 最近作成されたファイルのフルパスを返す
        import os
        abs_path = os.path.abspath(self.dir_path)
        os.chdir(abs_path)  
        recent_dir = sorted(os.listdir(), reverse=True)[0]
        path = os.path.abspath(os.path.join(abs_path, recent_dir))
        return path


    def deleteOldFiles(self, limits):
        # ファイルがlimitsを超えた場合超えた数だけ古いファイルを削除する
        import os
        if len(os.listdir(self.dir_path)) < limits: 
            return 
        os.chdir(self.dir_path)
        diff = len(os.listdir(self.dir_path)) - limits
        for i in range(diff):
            list_dir = sorted(os.listdir())
            os.remove(os.path.join(self.dir_path, list_dir[0]))
