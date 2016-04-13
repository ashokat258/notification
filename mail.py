import smtplib
from oslo_log import log as logging

LOG = logging.getLogger(__name__)

def func(String):
 FROM = "bobby"
 FROMMAIL= "bobby@haproxy.ashok.co.in"
 TO = "ashokt@haproxy.ashok.co.in"
 server = smtplib.SMTP('10.66.30.141', 587)
 server.starttls()
 server.login(FROM, "ashok")
 SUBJECT  = "INSTANCE INFORMATION"

 msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (FROMMAIL, ", ".join(TO), SUBJECT) )
 msg += "Please check the status of the instancein func\r\n"
 msg += String
 server.sendmail(FROMMAIL, TO, msg)
 LOG.debug("ASHOK:DEBUG MAIL SENT SUCCESSFULLY in func\n")
 print("ASHOK:DEBUG MAIL SENT SUCCESSFULLY in func\n")
 server.quit()

if __name__ == '__main__':
  func("BUILDING")

