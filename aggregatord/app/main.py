# main.py
# Entry point for aggregatord service
# defines the api gateway for client to access aggregator service

# call aggregator service here
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import model.aggregator as aggregator

# temporary hardcoded urls for iteminfod and stockinfod microservices
item_url = "http://iteminfod:8080/item-info"
stock_url = "http://stockinfod:8081/stock-info"

app = FastAPI()
aggregator_instance = aggregator.Aggregator(item_url, stock_url)

# create an api for this lookup function
@app.post("/lookup")
async def lookup(request: Request):
    # parse incoming json request
    data = await request.json()

    # extract productID
    productID = data.get("productID")

    # validate productID
    if not productID:
        return {"error": "productID is required"}
    
    # call aggregator's lookup method
    lookupResult, statusCode = aggregator_instance.lookup(productID)
    
    # return results of lookup
    return JSONResponse(status_code=statusCode, content=lookupResult)