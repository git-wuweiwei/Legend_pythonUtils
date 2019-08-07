# coding : utf-8

from src.legendUtils import sshUtil, mailUtils

hostname = '18.221.160.35'
username = 'ubuntu'
passwd = 'KaCAW446PHXBZc3@gsfWMydV'

ssh = sshUtil.sshConnectHost(hostname, username, passwd)





message = {}

xinxi = ssh.excute_cmd(['sh ~/.profile','cd /home/ubuntu/workspace/qtum/bin/qtum-cli','df -h'])

message['xinxi'] = xinxi
send = mailUtils.mailUtil('tusing@legenddigital.com.au', 'www_19920912')


# 'chenxinshutianyunwei@dingtalk.com'
print (send.send_mail(['tusing@legenddigital.com.au','chenxinshutianyunwei@dingtalk.com'],message))
