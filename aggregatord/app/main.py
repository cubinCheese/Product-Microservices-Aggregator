# main.py
# Entry point for aggregatord service
# defines the api gateway for client to access aggregator service

# call aggregator service here
import requests
import FastAPI
import model.aggregator as aggregator

app = FastAPI()
aggregator_instance = aggregator.Aggregator(item_url, stock_url)

# create an api for this lookup function
@app.post("/lookup")
async def lookup(request: FastAPI.Request):
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
    return lookupResult, statusCode