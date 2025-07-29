# email_alert.py
from gmail_auth import get_gmail_service
from email.mime.text import MIMEText
import base64

def create_message(sender, to, subject, body_text):
    message = MIMEText(body_text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": raw}

def send_email(subject, body_text, recipient_email):
    try:
        service = get_gmail_service()
        message = create_message("me", recipient_email, subject, body_text)
        service.users().messages().send(userId="me", body=message).execute()
        return True
    except Exception as e:
        print(f"[ERROR] Email sending failed: {e}")
        return False
