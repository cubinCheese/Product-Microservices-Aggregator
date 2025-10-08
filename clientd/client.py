import json
from typing import Dict
import requests

"""client.py

Simple container for three JSON test bodies used to exercise the aggregator
final-aggregation cases:

  1) Item Info = 404  -> product not found
  2) Item Info = 200 & Stock = 200 -> merged information
  3) Item Info = 200 & Stock = 404 -> available: 0

This file only creates the data structure `TEST_PAYLOADS` and exposes a tiny
helper to print them. Use these objects as the `json=` argument to `requests.post`.
"""

# Three JSON bodies for testing the aggregator endpoint
TEST_PAYLOADS: Dict[str, Dict[str, str]] = {
    # 1) Item Info = 404 (no product)
    "no_product": {"productID": "NOT_REAL_ID"},

    # 2) Item Info = 200 and Stock = 200 (merged information expected)
    "in_stock": {"productID": "XYZ-12345"},

    # 3) Item Info = 200 and Stock = 404 (item exists but out of stock)
    "out_stock": {"productID": "RQY-22222"},
}

def print_test_payloads():
    print("Available test payloads:\n")
    for name, payload in TEST_PAYLOADS.items():
        print(f"- {name}:")
        print(json.dumps(payload, indent=2))
        print()


if __name__ == "__main__":
    print_test_payloads()

    # helper to POST each payload to an aggregator URL and print the results
    def post_all_payloads(lookup_url: str = "https://aggregatord-19495045139.us-west2.run.app/lookup"):

        print(f"Posting {len(TEST_PAYLOADS)} payloads to {lookup_url}\n")
        for name, payload in TEST_PAYLOADS.items():
            try:
                resp = requests.post(lookup_url, json=payload, timeout=5)
            except requests.RequestException as e:
                print(f"{name}: REQUEST ERROR: {e}\n")
                continue

            print(f"{name}: HTTP {resp.status_code}")
            try:
                print(json.dumps(resp.json(), indent=2))
            except Exception:
                print(resp.text)
            print()

    # run against local by default
    post_all_payloads()

