import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up the credentials
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json')

# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('./credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# Create the Gmail service
service = build('gmail', 'v1', credentials=creds)

# Send the email
def prep_and_send_email(disease, soil_moisture):
    # Create message
    message = MIMEMultipart()
    message['to'] = 'abdalrhmanayoub41@gmail.com' 
    message['subject'] = 'Test email'
    message.attach(MIMEText(f"{disease} - {soil_moisture}"))
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()  
    try:
        message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        print('Email sent successfully')
        print('Message ID: %s' % message['id'])
    except HttpError as error:
        print('An error occurred:', error)   
        
# Call the function      
# prep_and_send_email("diseaseeee", "soil_moistureeee")