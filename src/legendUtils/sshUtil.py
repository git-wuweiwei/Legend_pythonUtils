# coding : utf-8

import paramiko
from paramiko.config import SSH_PORT

class sshConnectHost:

    def __init__(self, hostname, username, passwd, port=SSH_PORT):
        # 初始化ssh连接
        self.ssh = paramiko.SSHClient()
        # 允许连接不在信任列表的主机
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.ssh.connect(hostname=hostname,
                         username=username,
                         password=passwd,
                         port=port
                         )

    def excute_cmd(self, cmd):
        msg = ''
        for i in cmd:
            stdin, stdout, stderr = self.ssh.exec_command(i)
            stdout = stdout.read()
            stderr = stderr.read()
            msg += stdout.decode() + stderr.decode()
        return msg


    def expected_return(self,cmd=[], expect_message=''):
        message = self.excute_cmd(cmd)

        if expect_message is not None:
            if message.strip('\n').endswith(expect_message):
                return True

            return False
        return 'the except_message is None'





ssh = sshConnectHost(hostname='47.244.186.111',username='admin',passwd='cx8ALkh366adm!@#',port=4399)

# print (ssh.excute_cmd(['df -h','ls -l /']))


print (ssh.expected_return(cmd=['df -h'],expect_message='1000'))
