####-----------------------From Real PYtHON--------------------------

import email
import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = 'gpsData'
body = "This is an email with attachment sent from Python"
# sender_email = 'kalilinux70733@gmail.com'
# receiver_email = 'kalilinux70733@gmail.com'
sender_email = 'joshuakawalya766@gmail.com'
receiver_email = 'joshuakawalya766@gmail.com'
password = 'iecwnorbuyuanacs'

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

message.attach(MIMEText(body, "plain"))
filename = "gpsdata.txt"  # In same directory as script

# Open PDF file in binary mode
# Add file as application/octet-stream
# Email client can usually download this automatically as attachment
with open(filename, "rb")as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)
#Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition", f"attachment; filename={filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
