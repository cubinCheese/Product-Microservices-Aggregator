# client.py
# Entry point for clientd service
import requests
import json

# make sure that "docker run -it -p 8080:8080 check_prime" is running.
# then you can run this file (making a post request)

#url = "http://0.0.0.0:8080/prime"

# url targeting aggregator
lookup_url = "http://localhost:8000/lookup"

prod_id_val = input("Enter productID: ")

# send request for product id
payload = {"productID": prod_id_val}

response = requests.post(lookup_url, json=payload)

print(response.text)

