# send_sms.py
from twilio.rest import Client

def send_sms(message, to_number):
    account_sid = 'ACb21995dee1d1f71dd066cd34c522e565'
    auth_token = 'c98938d948d83888ce4cb432b7f6a3a7'
    from_number = '+17622132022'

    client = Client(account_sid, auth_token)
    
    try:
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print("SMS sent successfully.")
    except Exception as e:
        print(f"Error sending SMS: {e}")
