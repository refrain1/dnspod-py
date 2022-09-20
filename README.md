# dnspod-py
一个简易的dnspod python脚本，定时请求dnspod API接口实现DDNS

# 安装
### pip install apscheduler
### pip install requests

ssh进入群晖，将文件放至/volume1目录

## 修改main.py文件
```
# 域名
domain = ""
# token  组成样式为ID + "," + "TOKEN"
token = ""
# 记录类型
record_type = "AAAA"
# 提主机记录, 如 www，如果不传，默认为 @。
sub_domain = ""
# 记录线路，通过API记录线路获得，中文，比如：默认。
record_line = "默认"
```

## 运行
python3 /volume1/main.py
