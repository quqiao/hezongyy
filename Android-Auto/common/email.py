import time,os,sys
from email.mime.text import MIMEText #定义邮件内容
from email.header import Header #邮件主题
from email.mime.multipart import MIMEMultipart #附件
import smtplib
#from email import encoders

def send_mail(filename):
    mail_host = 'stmp.qq.com'
    mail_user = "553248560@qq.com"
    mail_pass = "worqlzmlixklbdgi"   # 在邮箱界面获取的授权码
    sender = "android自动化"  # 发送邮箱别名（用户名）
    receivers = ['553248560@qq.com']  # 收件人列表
    message = MIMEMultipart('related')  # 采用related定义内嵌资源的邮件体（附件）

    #  发送内容
    f = open(filename, 'rb')
    mail_body = f.read()
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename))
    # encoders.encode_base64(att) 加密
    message.attach(att)
    f.close()

    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    message.attach(msg)
    message['From'] = sender
    message["To"] =','.join(receivers)
    message['Subject'] = Header("android自动化测试报告","utf-8")
    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(mail_user, receivers, message.as_string())
    smtp.quit()

    #查找最新的测试报告
def report(testreport):
    lists = os.listdir(testreport)  # 返回指定文件夹下的文件或文件夹名称列表
    lists.sort(key=lambda fn: os.path.getatime(testreport + "/" + fn))  # 通过sort()方法按时间排序
    lists.reverse()
    filename = os.path.join(testreport, lists[0])
    print(filename, "发送成功")
    return filename
