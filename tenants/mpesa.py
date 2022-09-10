# import requests
# import json
# from requests.auth import HTTPBasicAuth
# from datetime import datetime
# import base64


# class MpesaC2bCredential:
#     consumer_key = 'k6fdlF5WZOwV9xGy9OUlQtozkAfdN4OA'
#     consumer_secret = 'MI2ba7QfDXa8c90N'
#     api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


# class MpesaAccessToken:
#     r = requests.get(MpesaC2bCredential.api_URL,
#                      auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
#     mpesa_access_token = json.loads(r.text)
#     validated_mpesa_access_token = mpesa_access_token['access_token']


# class LipanaMpesaPpassword:
#     lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
#     Business_short_code = "522522"
#     OffSetValue = '0'
#     passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

#     data_to_encode = Business_short_code + passkey + lipa_time

#     online_password = base64.b64encode(data_to_encode.encode())
#     decode_password = online_password.decode('utf-8')

# # response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Bearer cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ==' })
# # print(response.text.encode('utf8'))



# # mpesa = MpesaPayments(
# #     "522522",
# #     '',
# #      "k6fdlF5WZOwV9xGy9OUlQtozkAfdN4OA",
# #      "MI2ba7QfDXa8c90N", 
# #      "call_back_url", 
# #      "account_reference", 
# #      "transaction_desc"
# # ) 


# # class Mpesa:
# #     def __init__(self):
# #         self.mpesa = MpesaPayments(
# #             consumer_key='01au7vJAPlbbQupYFtOUr1dKOLZBorl6',
# #             consumer_secret='SobIDHttqJiUZDg1',
# #             host_name='https://myhostname',
# #             pass_key='Your pass key from daraja',
# #             safaricom_api='https://sandbox.safaricom.co.ke',
# #             short_code='174379'
# #         )

# #     def lipa_na_mpesa(self, phone_number, amount, account_reference, transaction_desc):
# #         response = self.mpesa.lipa_na_mpesa_online(
# #             phone_number=phone_number,
# #             amount=amount,
# #             account_reference=account_reference,
# #             transaction_desc=transaction_desc
# #         )
# #         return response

# #     def b2c(self, phone_number, amount, account_reference, transaction_desc):
# #         response = self.mpesa.b2c(
# #             phone_number=phone_number,
# #             amount=amount,
# #             account_reference=account_reference,
# #             transaction_desc=transaction_desc
# #         )
# #         return response

# #     def b2b(self, phone_number, amount, account_reference, transaction_desc):
# #         response = self.mpesa.b2b(
# #             phone_number=phone_number,
# #             amount=amount,
# #             account_reference=account_reference,
# #             transaction_desc=transaction_desc
# #         )
# #         return response

# #     def reversal(self, phone_number, amount, account_reference, transaction_desc):
# #         response = self.mpesa.reversal(
# #             phone_number=phone_number,
# #             amount=amount,
# #             account_reference=account_reference,
# #             transaction_desc=transaction_desc
# #         )
# #         return response

# #     def transaction_status(self, phone_number, amount, account_reference, transaction_desc):
# #         response = self.mpesa.transaction_status(
# #             phone_number=phone_number,
# #             amount=amount,
# #             account_reference=account_reference,
# #             transaction_desc=transaction_desc
# #         )
# #         return response