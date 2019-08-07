# coding : utf-8

import requests
import paramiko

hostname = '18.221.160.35'
username = 'ubuntu'
passwd = 'KaCAW446PHXBZc3@gsfWMydV'



ssh = paramiko.SSHClient()


ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=hostname,username=username,password=passwd)

stdin ,stdout , stderr = ssh.exec_command('df -h')

stdout = stdout.read()

print (stdout.decode())
