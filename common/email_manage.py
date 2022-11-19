"""
邮件发送

"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common import conf


class EmailManage:

    def send_email(self):
        # 读取测试报告中的内容作为邮件的内容
        with open(conf.TEST_REPORT_PATH, 'r', encoding='utf8') as f:
            mail_body = f.read()
            print(mail_body)
        # 定义SMTP服务器
        smtpserver = 'smtp.163.com'
        # 发送邮件的用户名和授权密码
        username = '18344186993@163.com'
        password = 'IDUQQNYCCTVGPIBO'
        # 接收邮件的邮箱
        receiver = '825510546@qq.com'
        # 创建邮件对象
        message = MIMEMultipart('related')
        subject = 'pytest测试报告'
        fujian = MIMEText(mail_body, 'html', 'utf-8')  # 附件
        # 把邮件信息组装到邮件对象里
        message['from'] = username
        message['to'] = receiver
        message['Subject'] = subject
        # 附件填充
        message.attach(fujian)
        # 登录SMTP服务器
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(username, receiver, message.as_string())
        smtp.quit()


if __name__ == '__main__':
    EmailManage().send_email()
