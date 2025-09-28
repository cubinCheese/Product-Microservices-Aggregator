# stockinfo.py
# Model logic for stockinfo microservice
import csv

# Retrieves data from stock.csv and stores in local data structure
# In reality, data is queried from a database.

class StockInfoService:
    def __init__(self, stock_data={}):
        # Local Data storage for stock.csv
        self.stock_data = stock_data

    # Load CSV data into local dictionary data structure
    def load_csv_data(self, csv_file):
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            self.stock_data = {row['productID']: {"productID": row['productID'], "available": row['available']} for row in reader}

    # access stock.csv data and retrieve stock info by productID
    def get_item(self, productID):
        item = self.stock_data.get(productID, None)
        if item:
            return item, 200
        return {"error": "Product not found"}, 404



