import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()

msg['Subject'] = 'duanx'
msg['From'] = 'workinform@163.com'
msg['To'] = 'linhanqiu1123@163.com'
content = 'hedassdaasdsadd'
txt = email.mime.text.MIMEText(content)  
msg.attach(txt)  

#smtp = smtplib  
smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com', '25')
smtp.login('workinform@163.com', 'linhanqiu1123')
smtp.sendmail('workinform@163.com', 'linhanqiu1123@163.com', msg.as_string())
smtp.quit()  
print('邮件发送成功email has send out !')  