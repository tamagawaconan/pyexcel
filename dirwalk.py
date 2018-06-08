import os

HOMEDIR = '/Users/kawachi/Documents'

# HOMEDIRで指定したフォルダ配下のExcelファイル名一覧を出力
for foldername, subfolders, filenames in os.walk(HOMEDIR):
        for filename in filenames:
            ext = os.path.splitext(filename)
            if ext[1] == '.xlsx':
                print(foldername + '/' + filename)
