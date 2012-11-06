import smtplib

server = smtplib.SMTP('smtpserver.uit.no')
server.sendmail(from_addr='raboof@foobar.org', 
        to_addrs='jonas.juselius@uit.no',
        msg="""To: jonas.juselius@uit.no
From: raboof@foobar.org
Subject: The flea and the fly
A flea and a fly in a flue,
Were trapped and knew not what to do,
'Let us flee', said the fly,
'Let us fly', said the flea,
So they flew through a flaw in the flue.
""")
server.quit()
