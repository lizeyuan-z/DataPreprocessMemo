import datetime

# 按一定格式获取当前时间（前n时/分/秒）
(datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
(datetime.datetime.now() - datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
(datetime.datetime.now() - datetime.timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# 输出：
# '2023-11-02 16:45:55'， '2023-11-02 17:45:55'
