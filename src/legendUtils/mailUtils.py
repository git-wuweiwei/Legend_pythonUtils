# coding : utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


# class mailUtils:
#
#     def __init__(self,userName,passwd):
#         self.username = userName
#         self.passwd = passwd
#
#     def send_mail(self,):
#         pass


class mailDingDingUtils:


    def __init__(self,userName,passwd):
        self.userName = userName
        self.passwd = passwd

        # 固定的钉钉服务器地址
        self.host = "smtp.mxhichina.com"

        # 邮件内容
        self.mail = MIMEMultipart()

        # 初始化邮件链接服务
        self.smtp = smtplib.SMTP()




    def create_mail(self,send_user, recive_users, subjet='' ,content={}):
        self.mail['From'] = send_user
        self.mail['To'] = recive_users.append(self.userName)
        self.mail['subject'] = subjet

        for key in content.keys():
            self.mail.attach(MIMEText(str(key).rjust(50,"*") + '\n' +
                                      content[key] + '\n',
                                      "plain", "utf-8"))


    def send_mail(self) :
        """
        :param subject : 邮件内容信息
        :param recivers: 接受者，默认为列表
        :return: msg : 不成功返回异常信息
        """

        if self.mail['From'] is None or self.mail['To'] is None :
            print ("the mail is not initable,邮件未初始化")
            return

        msg = ''

        self.smtp.connect(self.host)
        self.smtp.login(self.userName,self.passwd)
        self.smtp.sendmail(from_addr=self.userName,to_addrs=self.userName,msg=self.mail.as_string())
        msg += 'the mail send successful'
        return msg

