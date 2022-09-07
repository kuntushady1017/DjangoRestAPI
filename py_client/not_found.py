import requests



endpoint = "http://localhost:8000/api/products/1/" #http://127.0.0.1:8000/


# getResponse = requests.get(endpoint, json={"product_id":13}) #HTTP Request

getResponse = requests.get(endpoint) #HTTP Request


print(getResponse.text) #prints raw response text

print(getResponse.headers)

# print(getResponse.json()) #prints raw response text

print(getResponse.status_code) #prints response status code
