import requests



endpoint = "http://localhost:8000/api/products/2/update/" #http://127.0.0.1:8000/

data={
    'title': 'Nike Jordan 360'
}
# getResponse = requests.get(endpoint, json={"product_id":13}) #HTTP Request

getResponse = requests.put(endpoint, json=data) #HTTP Request


print(getResponse.text) #prints raw response text

# print(getResponse.headers)

# print(getResponse.json()) #prints raw response text

print(getResponse.status_code) #prints response status code
