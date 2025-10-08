test:
	# should return 200
	@curl -i -X POST "https://aggregatord-19495045139.us-west2.run.app/lookup" -d '{"productID":"XYZ-12345"}' -H "Content-Type: application/json" >> "maketest_results.txt"
	
	# 1. Test for productID "ABC-67890" (SuperClean Spray, available: 50)
	# Expected: HTTP 200, name: "SuperClean Spray", available: 50
	@curl -i -X POST "https://aggregatord-19495045139.us-west2.run.app/lookup" -d '{"productID":"ABC-67890"}' -H "Content-Type: application/json" >> "maketest_results.txt"

	# Test for productID "DEF-11111" (UltraSoft Towels, available: 0)
	# Expected: HTTP 200, name: "UltraSoft Towels", available: 0
	@curl -i -X POST "https://aggregatord-19495045139.us-west2.run.app/lookup" -d '{"productID":"DEF-11111"}' -H "Content-Type: application/json" >> "maketest_results.txt"

	# 3. Test for a non-existent productID (should return 404)
	# Expected: HTTP 404, error: "Product not found"
	@curl -i -X POST "https://aggregatord-19495045139.us-west2.run.app/lookup" -d '{"productID":"NOT_REAL_ID"}' -H "Content-Type: application/json" >> "maketest_results.txt"

	# 4. Test for productID "XYZ-12345" (Amayon Basics Wipes, available: 210)
	# Expected: HTTP 200, name: "Amayon Basics Wipes", available: 210
	@curl -i -X POST "https://aggregatord-19495045139.us-west2.run.app/lookup" -d '{"productID":"XYZ-12345"}' -H "Content-Type: application/json" >> "maketest_results.txt"

	# 5. Test for productID "RQY-22222" (FreshScent Detergent exists in items.csv but missing in stock.csv)
	# Expected: HTTP 200, name: "FreshScent Detergent", available: 0
	@curl -i -X POST "https://aggregatord-19495045139.us-west2.run.app/lookup" -d '{"productID":"RQY-22222"}' -H "Content-Type: application/json" >> "maketest_results.txt"
