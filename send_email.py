# import smtplib
# from email.mime.text import MIMEText

# def send_email(name, email, choice, rating, commets):
#     port = 2525
#     smtp_server = 'smtp.mailtrap.io'
#     login = '50f11615909096'
#     password = 'b2ea170002198a'
#     message = f"<h3>New Feedback Submission</h3><ul><li>Name: {name}</li><li>email: {email}</li><li>Rating: {rating}</li><li>comments: {commets}</li><li>choice: {choice}</li></ul>"

#     sender_email = '100kunday@gmail.com'
#     receiver_email = '100kunday@gmail.com'
#     msg = MIMEText(message, 'html')
#     msg['Subject'] = 'Feedback'
#     msg['From'] = sender_email
#     msg['To'] = receiver_email

#     # Send email
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.login(login, password)
#         server.sendmail(sender_email, receiver_email, msg.as_string())import smtplib, ssl
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(name, email, choice, rating, commets):
    sender_email = "testpythonmail1@gmail.com"
    receiver_email = "100kunday@gmail.com"
    password = '123Test123'
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email


    message["To"] = receiver_email
    sms = f"<h3>New Feedback Submission</h3><ul><li>Name: {name}</li><li>email: {email}</li><li>Rating: {rating}</li><li>comments: {commets}</li><li>choice: {choice}</li></ul>"
# Create the plain-text and HTML version of your message
    text = "TEST"

# Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(sms, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

# Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
           sender_email, receiver_email, message.as_string()
        )
