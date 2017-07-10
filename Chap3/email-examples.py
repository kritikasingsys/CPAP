#!/usr/bin/env python3
'email-examples.py - demo creation of email messages'
'Textbook had this in Python2, I ported it to Python3.'

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

#multipart alternative: text and html
def make_mpa_msg():
    email = MIMEMultipart('alternative')
    '''if 'alternative' is not passed, each of the two parts will be a separate
    attachment, so some email systems will show both'''
    text = MIMEText('Hello, World!\r\n', 'plain')
    email.attach(text)

    html = MIMEText('<html><body><h4>Hello, World!</h4></body></html>', 'html')
    email.attach(html)
    return email

#multpart: images
def make_img_msg(fn):
    with open(fn, 'rb') as f:
        data = f.read()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition', 'attachment; filename="%s"' % fn)
    return email

def sendMsg(fr, to, msg):
    s = SMTP('smtp.gmail.com')
    s.starttls()
    s.login('saurabh.chaturvedi63@gmail.com', 'ImNotGonnaRevealMyPassword')
    errs = s.sendmail(fr, to ,msg)
    assert len(errs) == 0, errs #not in book
    s.quit()

if __name__ == "__main__":
    print("Sending multipart alternative msg...")
    msg = make_mpa_msg()
    un = 'saurabh.chaturvedi63@gmail.com'
    msg['From'] = un
    rcps = [un, '16ucc086@lnmiit.ac.in']
    msg['To'] = ', '.join(rcps)
    msg['Subject'] = 'multipart alternative test'
    sendMsg(un, rcps, msg.as_string())

    print('Sending image msg...')
    msg = make_img_msg('screenShot.png')
    msg['From'] = un
    msg['To'] = ', '.join(rcps)
    msg['Subject'] = 'image file test'
    sendMsg(un, rcps, msg.as_string())
