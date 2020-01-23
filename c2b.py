import requests
import key
import lipa_na_mpesa

# register endpoints that safaricom will use to hit your server

def register_endpoints():
    access_token = lipa_na_mpesa.myaccesstoken
    api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "ShortCode": key.c2bshortcode,
    "ResponseType": "Completed",
    "ConfirmationURL": "http://otikojairus.com/pay/confirmationendpoint",
    "ValidationURL": "http://otikojairus.com/pay/validationurl"}

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

register_endpoints()

# simulate the payment process
def pay():
    access_token = lipa_na_mpesa.myaccesstoken
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "ShortCode":key.c2bshortcode,
    "CommandID":"CustomerPayBillOnline",
    "Amount":"45",
    "Msisdn":key.msisdn,
    "BillRefNumber":"4646464" }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

pay()