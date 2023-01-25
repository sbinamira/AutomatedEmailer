import ssl, smtplib
from email.message import EmailMessage

#read my email and password to authenticate gmail
with open('info.txt', 'r') as file:
    info = file.read().splitlines()
    email_sender = info[0]
    email_password = info[1]

#read the list of email receivers
with open('ppl2.txt', 'r') as file:
    email_receiver_list = file.read().splitlines()

#read voucher from file
with open('voucher2.txt', 'r') as file:
    voucher = file.read().splitlines()

subject = 'ISSessions THM Voucher'

vCount = 0
for email_receiver in email_receiver_list:
    msg = EmailMessage()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
    
    body = """
    Hello,

    Congratulations on being one of the top 100 users in the ISSessions CTF 2023! As a token of our appreciation, please accept this 1-month subscription for TryHackMe.

    Voucher code: {v}

    If there are any issues with the voucher, please let me know.

    Thanks,

    Shawn""".format(v=voucher[vCount])
    
    vCount += 1
    msg.set_content(body)

    #save which recipient gets which voucher
    with open('email2.txt', 'a') as file:
        file.write(email_receiver + '----------' + voucher[vCount]+"\n")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, msg.as_string())