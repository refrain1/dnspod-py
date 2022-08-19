import requests, json, pprint
from apscheduler.schedulers.background import BlockingScheduler
# 域名
domain = "tyxyq.com"
# token  组成样式为ID + "," + "TOKEN"
token = "337539,9141a0db54bc989c41347a797b9a1947"
# 记录类型
record_type = "AAAA"
# 提主机记录, 如 www，如果不传，默认为 @。
sub_domain = "v6"
# 记录线路，通过API记录线路获得，中文，比如：默认。
record_line = "默认"


def ddns():
    domain_rep = requests.get('https://6.ipw.cn/')

    data = {
        "login_token": token,
        "format": "json",
        "domain": domain,
    }

    rep = requests.post('https://dnsapi.cn/Record.List', data=data)

    records = json.loads(rep.text)['records']

    data = {
        "login_token": token,
        "format": "json",
        "domain": domain,
        "record_id": "",
        "record_type": record_type,
        "sub_domain": sub_domain,
        "record_line": record_line,
        "value": domain_rep.text,
    }

    for i in records:
        if i['name'] == data['sub_domain']:
            data['record_id'] = i['id']
    r = requests.post('https://dnsapi.cn/Record.Modify', data=data)
    pprint.pprint(json.loads(r.text))


if __name__ == "__main__":
    ddns()
    scheduler = BlockingScheduler()
    job = scheduler.add_job(ddns, trigger='interval', minutes=5)
    scheduler.start()
