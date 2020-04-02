# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:04:10 2020

@author: jiang
"""

import smtplib
from email.mime.text import MIMEText


MailtoList = ['nico20jby@163.com']
MailHost = 'smtp.sina.com'
MailUser = 'jiangby03@sina.com'
MailPass = 'rOni20070110'


msg = MIMEText('你好')
msg['Subject'] = ('你好')
msg['From'] = MailUser
msg['To'] = ';'.join(MailtoList)


s = smtplib.SMTP()

s.connect(MailHost)
s.login(MailUser, MailPass)
s.sendmail(MailUser, MailtoList, msg.as_string())
s.close()
print('成功')

'''
try:
    S = smtp.SMTP()
    S.connect(MailHost)
    S.login(MailUser, MailPass)
    S.sendmail(MailUser, MailtoList, msg.as_string())
    S.close()
    print('Submission Success')

except Exception:
    print(str(Exception))
    print('Submission Fail')
'''










