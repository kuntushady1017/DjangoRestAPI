import requests



endpoint = "http://localhost:8000/api/products/" #http://127.0.0.1:8000/


data = {
    "title":"Nike short",
}
getResponse = requests.post(endpoint, json=data) #HTTP Request


# print(getResponse.text) #prints raw response text

# print(getResponse.headers)

print(getResponse.json()) #prints raw response text

print(getResponse.status_code) #prints response status code
