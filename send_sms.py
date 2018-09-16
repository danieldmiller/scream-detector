# Download the helper library from https://www.twilio.com/docs/python/install

#Getting data

import sys



from twilio.rest import Client

def send_sms(num):
    num = num * 5

    # Your Account Sid and Auth Token from twilio.com/console

    account_sid = 'AC0f5c0d5df88b622191d053d98c4e0b0b'

    auth_token = '796db0a4cd1b492d14f2f3248ab2f70b'

    client = Client(account_sid, auth_token)



    message = None



    if 2 < int(num):
        message = client.messages \
			.create(
				body="Dispatch Officers to Location of apple.",
				from_='+15067006521',
				to='+14039736465'
			)

    if(message is not None):
        print(message.sid)


send_sms(float(sys.argv[1]))
#while(cameraIsOpen)

    #
