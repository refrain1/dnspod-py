# dnspod-py
一个简易的dnspod python脚本，定时请求dnspod API接口实现DDNS

# 安装
### pip install apscheduler
### pip install requests

ssh进入群晖，将文件放至/volume1目录

## 修改main.py文件
```
# 域名
domain = "你的域名"
# token  组成样式为ID + "," + "TOKEN"
token = "组成样式为ID + "," + "TOKEN""
# 记录类型
record_type = "AAAA"
# 提主机记录, 如 www，如果不传，默认为 @。
sub_domain = ""
# 记录线路，通过API记录线路获得，中文，比如：默认。
record_line = "默认"
```

## 运行
### 新建任务计划->用户自定义脚本
![image](https://user-images.githubusercontent.com/32951222/191224264-2c823c97-59eb-48d1-a0d3-382204efd419.png)

### 点击计划->修改为如下
![image](https://user-images.githubusercontent.com/32951222/191224611-e0605180-14cd-4423-8f7a-f67131169174.png)
### 点击任务设置，修改为如下

![image](https://user-images.githubusercontent.com/32951222/191224708-cd979fe0-edfd-466f-8068-3fc7cbfbc7d6.png)

python3 /volume1/main.py
