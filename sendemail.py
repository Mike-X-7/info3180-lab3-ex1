import smtplib

fromaddr = 'likemike303@gmail.com'
toaddr = 'likemike303@gmail.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
fromname ="Michael Green"
fromaddr = 'likemike303@gmail.com'
toname = "Michael Green"
toaddr='likemike303@gmail.com'
subject = "lab3-ex1"
msg = "lab3-ex1 completed!!! "
messagetosend = message.format(

 fromname,
 fromaddr,
 toname,
 toaddr,
 subject,
 msg)

# Credentials (if needed)
# Username and password removed for privacy purposes.
username = ''
password = ''

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()