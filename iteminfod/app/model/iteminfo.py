# iteminfo.py
# Model logic for iteminfo microservice
import csv

# Retrieves data from items.csv and stores in local data structure
# In reality, data is queried from a database.

class ItemInfoService:
    def __init__(self, items_data={}):
        # Local Data storage for items.csv
        self.items_data = items_data

    # Load CSV data into local dictionary data structure
    def load_csv_data(self, csv_file):
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            self.items_data = {row['productID']: {"productID": row['productID'], "name": row['name']} for row in reader}
    
    # access items.csv data and retrieve item info by productID
    def get_item(self, productID):
        item = self.items_data.get(productID, None)
        if item:
            return item, 200
        return {"error": "Product not found"}, 404


