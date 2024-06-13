from twilio.rest import Client

account_sid = 'AC1cecfbc7f86f177c288ee2064797e6c9'
auth_token = '6b555ee2e00ce3ffcc416a96fbba9a97'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Estou enviando aquiii ',
  to='whatsapp:+5512991471392'
)

print(message.sid)