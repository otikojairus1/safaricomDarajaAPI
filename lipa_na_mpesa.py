import requests
import keys
import datetime
import base64
from requests.auth import HTTPBasicAuth


timestamp = datetime.datetime.now()
formated_time = timestamp.strftime('%Y%m%d%H%M%S')
# print(formated_time)

password_tokens =  '174379' + 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919' + formated_time
encode_password = base64.b64encode(password_tokens.encode())
decoded_password = encode_password.decode()
# print(decoded_password)


#getting access tokens

 
  

consumer_key = "Netim85fhoDMevXP4GjGVZ5YjDpIgbx7"
consumer_secret = "bUyeUr96Jnn6TunM"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

responce = r.json()
myaccesstoken = responce['access_token']
  

#pushin stk
access_token = myaccesstoken
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % access_token }
request = {
"BusinessShortCode": "174379",
"Password": decoded_password,
"Timestamp": formated_time,
"TransactionType": "CustomerPayBillOnline",
"Amount": "45",
"PartyA": "254722753364",
"PartyB": "174379",
"PhoneNumber": "254722753364",
"CallBackURL": "https://otiko.com/pay",
"AccountReference": "546464647",
"TransactionDesc": "pay fees"
}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)
  