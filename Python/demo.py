'''lst=["my day was horrible","I am sad","I don't feel very well","I am disappointed"]
nlst=[]
for i in lst:
    for j in i.split(" "):
        nlst.append(j)
unik=set(nlst)
for i in unik:
    print(i,nlst.count(i))'''
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages('MM800f449d0399ed014aae2bcc0cc2f2ec').fetch()

print(message.body)