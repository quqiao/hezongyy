import os
import win32com.client as win32
import datetime
import readConfig
import getpathInfo
from common1.Log import logger
from email.mime.text import MIMEText #定义邮件内容
from email.header import Header  # 邮件主题
from email.mime.multipart import MIMEMultipart  # 附件
import smtplib


read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')#从配置文件中读取，邮件主题
app = str(read_conf.get_email('app'))#从配置文件中读取，邮件类型
addressee = read_conf.get_email('addressee')#从配置文件中读取，邮件收件人
cc = read_conf.get_email('cc')#从配置文件中读取，邮件抄送人
mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')#获取测试报告路径
logger = logger

class send_email():
    def outlook(self):
        olook = win32.Dispatch("%s.Application" % app)
        mail = olook.CreateItem(win32.constants.olMailItem)
        mail.To = addressee  # 收件人
        mail.CC = cc  # 抄送
        mail.Subject = str(datetime.datetime.now())[0:19]+'%s' %subject#邮件主题
        mail.Attachments.Add(mail_path, 1, 1, "myFile")
        content = """
                执行测试中……
                测试已完成！！！
                生成报告中……
                报告已生成……
                报告已邮件发送！！
                """
        mail.Body = content
        mail.Send()
        print('send email ok!!!!')
        logger.info('send email ok!!!!')

def qq_send_mail(filename):
    mail_host = 'stmp.qq.com'
    mail_user = "553248560@qq.com"
    mail_pass = "lglwxlqixsjxbbid"  # 在邮箱界面获取的授权码
    sender = "seleniumWeb自动化测试"  # 发送邮箱别名（用户名）
    receivers = ['553248560@qq.com']  # 收件人列表
    message = MIMEMultipart('related')  # 采用related定义内嵌资源的邮件体 （附件）

    # 发送内容
    f = open(filename, 'rb')
    mail_body = f.read()
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'  # 附件格式
    att.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename))
    # encoders.encode_base64(att) 加密
    message.attach(att)  # 发送附件
    f.close()

    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    message.attach(msg)
    message['From'] = sender
    message["To"] = ','.join(receivers)
    message['Subject'] = Header("药易购新平台开发API接口测试报告", "utf-8")
    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(mail_user, receivers, message.as_string())
    smtp.quit()

    # 查找最新的测试报告

def qq_report(testreport):
    lists = os.listdir(testreport)  # 返回指定文件夹下的文件或文件夹名称列表
    lists.sort(key=lambda fn: os.path.getatime(testreport + "/" + fn))  # 通过sort()方法按时间排序
    lists.reverse()
    filename = os.path.join(testreport, lists[0])
    print(filename, "发送成功")
    return filename


if __name__ == '__main__':  # 运营此文件来验证写的send_email是否正确
    print(subject)
    send_email().outlook()
    print("send email ok!!!!!!!!!!")