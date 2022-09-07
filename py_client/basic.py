import requests

#endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" #http://127.0.0.1:8000/


# getResponse = requests.get(endpoint, json={"product_id":13}) #HTTP Request

getResponse = requests.post(endpoint, json={"title":"Nike Socks", 
"content":"Feel warm on your feet with new Nike Sock",
"price":9.25}) #HTTP Request


print(getResponse.text) #prints raw response text

print(getResponse.headers)

# print(getResponse.json()) #prints raw response text

print(getResponse.status_code) #prints response status code
