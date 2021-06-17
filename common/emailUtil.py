# -*- coding: UTF-8 -*-

"""
    @create：2020-05-14 9:50
    @author：by aries
    @description：发送测试报告邮件

"""

import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

class EmailSolution():
    def __init__(self, username, passwd, to_receiver, cc_receiver, title, content, file=None, ssl=False,
                 email_host='smtp.qq.com', port=25, ssl_port=465):
        """
        :param username: 用户名
        :param passwd: 密码
        :param to_receiver: 收件人，多个要传list ['a@qq.com','b@qq.com]
        :param cc_receiver: 抄送人，多个要传list ['a@qq.com','b@qq.com]
        :param title: 邮件标题
        :param content: 邮件正文
        :param file: 附件路径，如果不在当前目录下，要写绝对路径，默认没有附件
        :param ssl: 是否安全链接，默认为普通
        :param email_host: smtp服务器地址，默认为qq服务器
        :param port: 非安全链接端口，默认为25
        :param ssl_port: 安全链接端口，默认为465
        """

        self.username = username
        self.passwd = passwd
        self.to_receiver = to_receiver
        self.cc_receiver = cc_receiver
        self.title = title
        self.content = content
        self.file = file
        self.email_host = email_host
        self.port = port
        self.ssl = ssl
        self.ssl_port = ssl_port

    def send_mail(self):
        msg = MIMEMultipart()
        #发送内容的对象
        if self.file:
            file_name = os.path.split(self.file)[-1]
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('Error:Attachment cannot be opened.')
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                # base64.b64encode(file_name.encode()).decode()
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                att["Content-Disposition"] = 'attachment; filename="%s"'%(new_file_name)
                msg.attach(att)
        msg.attach(MIMEText(self.content, _subtype="html", _charset="utf-8"))
        msg['Subject'] = self.title
        msg['From'] = self.username
        msg['To'] = ','.join(self.to_receiver)
        msg['Cc'] = ','.join(self.cc_receiver)
        receiver = self.to_receiver + self.cc_receiver

        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)

        #发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, receiver, msg.as_string())
            # pass
        except Exception as e:
            print('Error...', e)
        else:
            print('Sent successfully!')
        self.smtp.quit()
