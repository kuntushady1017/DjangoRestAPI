import requests

product_id = input("What product do want to delete \n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not found')

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/" #http://127.0.0.1:8000/


    # getResponse = requests.get(endpoint, json={"product_id":13}) #HTTP Request

    getResponse = requests.delete(endpoint) #HTTP Request

    print(getResponse.status_code, getResponse.status_code==204) #prints response status code
