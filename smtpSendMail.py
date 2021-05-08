from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

import socket

def getIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('www.baidu.com',0))
    ip = s.getsockname()[0]
    s.close()
    return ip

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def sendMail():
    from_addr = "rolanky@sina.com"
    password = "ea06b29df2dff13f"
    to_addr = "1435959447@qq.com"
    smtp_server = "smtp.sina.com"

    msg = MIMEText(getIp(), 'plain', 'utf-8')
    msg['From'] = _format_addr('roma-swj-nas <%s>' % from_addr)
    msg['To'] = _format_addr('Rolanky <%s>' % to_addr)
    msg['Subject'] = Header('nasIp', 'utf-8').encode()
        
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

if __name__=="__main__":
    if 1:
        sendMail()
    else:
        print("wait and no send")
