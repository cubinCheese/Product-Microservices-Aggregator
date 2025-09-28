# main.py
# Entry point for iteminfod service

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.iteminfo import ItemInfoService
import os

app = FastAPI()

# Path to items.csv (adjust if needed)
CSV_PATH = os.path.join(os.path.dirname(__file__), "items.csv")

# Initialize service and load data
item_service = ItemInfoService()
item_service.load_csv_data(CSV_PATH)

# Define API endpoint route
@app.get("/item-info/items/{productID}")
def get_item(productID: str):
    item, statusCode = item_service.get_item(productID)
    if item:
        return JSONResponse(status_code=statusCode, content=item)
    return JSONResponse(status_code=statusCode, content={"error": "Product not found"})
