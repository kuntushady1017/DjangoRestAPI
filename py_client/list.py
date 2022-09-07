from email import header
from wsgiref import headers
import requests
from getpass import getpass


authEndPoint = "http://localhost:8000/api/auth/"
username  = input("Enter your username \n")
password = getpass("Enter password \n")

authResponse = requests.post(authEndPoint, json={"username":username, "password": password}) #HTTP Request

print(authResponse.json(), ) #prints raw response text
if authResponse.status_code == 200:
    token = authResponse.json()['token'] 
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/" #http://127.0.0.1:8000/
    getResponse = requests.get(endpoint, headers=headers) #HTTP Request
    print(getResponse.text) #prints raw response text

    # print(getResponse.headers)


    print(getResponse.status_code) #prints response status code
