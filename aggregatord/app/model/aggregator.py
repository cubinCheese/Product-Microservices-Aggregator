# aggregator.py
# Model logic for aggregator
import requests

# Queries microservices (iteminfod, stockinfod, clientd) to complete requests and provide results
# Aggregator aggregates results from microservices and returns them to client
# acting as a middleman/orchestrator between client and microservices
class Aggregator:
    def __init__(self, item_url, stock_url):
        self.item_url = item_url    # url for requested item information
        self.stock_url = stock_url  # url for requested stock information

    def lookup(self, productID):

        # Query iteminfod microservice
        item_url = f"{self.item_url}/items/{productID}"
        item_response = requests.get(item_url)
        if item_response.status_code == 404:
            return {"error": "Product not found"}, 404
        item_data = item_response.json()

        # Query stockinfod microservice
        stock_url = f"{self.stock_url}/items/{productID}"
        stock_response = requests.get(stock_url)
        if stock_response.status_code == 404:
            # Item exists, but stock not found: available = 0
            return {
                "productID": productID,
                "name": item_data["name"],
                "available": 0
            }, 200
        stock_data = stock_response.json()

        # (You usually don't need to query clientd from aggregator)

        # Aggregate results
        lookupResult = {
            "productID": productID,
            "name": item_data["name"],
            "available": stock_data["available"]
        }
        statusCode = 200

        return lookupResult, statusCode