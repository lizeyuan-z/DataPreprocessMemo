import os


# 对文件按创建时间进行排序
files = os.listdir(dir_path)
files.sort(key=lambda x: os.path.getctime(os.path.join(dir_path, x)))
