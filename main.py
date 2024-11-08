import smtplib

sender = "shiamsharif.dev@gmail.com"
receiver = "siksumaya@gmail.com"
password = "Your_App_Password"  # Use an app password if 2FA is enabled

subject = "Python Email Test"
body = "I wrote an email! :D \n kal ke dhore ey kaj ta korchilam but hocccelo nah aj ke holo..."

# Corrected "message" and formatting
message = f"""\
From: Shiam Sharif <{sender}>
To: {receiver}
Subject: {subject}

{body}
"""

# Connect to the Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Login successful")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in! Check your credentials or app password settings.")
finally:
    server.quit()  # Make sure to close the connection
