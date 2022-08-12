import base64
import mimetypes
import os
from email.message import EmailMessage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.oauth2.credentials import Credentials
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

TOKEN_FILE = "token.json"

def send_mail(fromaddr, toaddr, subject, message, filepath=""):
    SCOPES = [
        "https://www.googleapis.com/auth/gmail.modify",
        "https://www.googleapis.com/auth/gmail.readonly",
        "https://www.googleapis.com/auth/gmail.labels",
        "https://www.googleapis.com/auth/gmail.metadata",
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/gmail.send'
    ]

    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    # create gmail api client
    service = build('gmail', 'v1', credentials=creds)
    mime_message = EmailMessage()

    # headers
    mime_message['To'] = toaddr
    mime_message['From'] = fromaddr
    mime_message['Subject'] = subject

    # text
    mime_message.set_content(message)
    
    if filepath != "":
        filename = os.path.basename(filepath)

        maintype, subtype = "application", "octet-stream"

        with open(filepath, 'rb') as fp:
            attachment_data = fp.read()

        mime_message.add_attachment(attachment_data, maintype, subtype, filename=filename)

    encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()

    body_msg = {
        'raw': encoded_message
    }
    # pylint: disable=E1101
    send_message = (
        service.users().messages()
        .send(userId="me",body=body_msg)
        .execute()
    )
    print("Email send!")
    print(F'Message Id: {send_message["id"]}')