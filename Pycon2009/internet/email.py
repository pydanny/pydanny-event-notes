import smtplib
from settings import *

def pop():
    from poplib import POP3_SSL as POP3
    from settings import *

    s = POP3('pop.gmail.com', 995)
    s.user(un)
    s.pass_(pw)
    rv, msg, sz = s.retr(336)

    print '-' * 25
    for line in msg:
        print line
    print  '-' * 25
    s.quit()


###################

def imap():
    from imaplib import IMAP4_SSL as IMAP4
    from settings import *
    s = IMAP4('imap.gmail.com', 993)
    s.login(un, pw)
    s.select()
    typ, data = s.fetch('264', '(RFC822)')
    print '-' * 25
    for line in data[0][1].splitlines():
        print line
    print '-' * 25
    s.close()
    s.logout()

######################
# sending to gmail

def smtp():
    


    from_ = 'pydanny@gmail.com'
    to = [from_]

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(un,pw)
    s.sendmail(from_, to, 'I am danny')
    s.close()
    
smtp()