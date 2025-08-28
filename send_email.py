import smtplib, ssl, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
port = int(os.getenv("SMTP_PORT", "587"))
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
password = os.getenv("EMAIL_PASSWORD")

message = MIMEMultipart("alternative")
message["Subject"] = "Test Email from Python"
message["From"] = sender_email
message["To"] = receiver_email

text = "Hello, this is a test email sent from Python script using SMTP."
part1 = MIMEText(text, "plain")
message.attach(part1)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("✅ Email sent successfully!")
