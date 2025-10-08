# Docker Setup & Testing Instructions
## 0. 
    While in the main project root directory...
## 1. Build Docker Images

```bash
docker build -t iteminfod ./iteminfod
docker build -t stockinfod ./stockinfod
docker build -t aggregatord ./aggregatord
```

## 2. Create Docker Network

```bash
docker network create microservices-net
```

- Note: This needs to be done to avoid "Internal Server Error" due to aggregator being unable to reach the port which microservices are run on.

## 3. Run Microservices on the Network

```bash
docker run --name iteminfod --network microservices-net -p 8080:8080 iteminfod
docker run --name stockinfod --network microservices-net -p 8081:8081 stockinfod
docker run --name aggregatord --network microservices-net -p 8082:8082 aggregatord
```

## 4. Test Aggregator Endpoint

```bash
curl -X POST http://localhost:8082/lookup -d '{"productID":"XYZ-12345"}' -H "Content-Type: application/json"
```

**Notes:**
- If you get a container name conflict, remove the old container:
	```bash
	docker rm <container_name>
	```
- Make sure all services are running before testing.


Testing on GCloud deployed services



# Google Cloud Deployment & Testing Instructions

## 0. Create a New Project 
- Created with name 'microservices-aggregator'

## 1. Authenticate and Set Project

```bash
gcloud auth login
gcloud config set project microservices-aggregator
gcloud auth configure-docker us-west2-docker.pkg.dev
```

## 2. Create Artifact Registry Repository

```bash
gcloud artifacts repositories create microservices-repo \
	--repository-format=docker --location=us-west2 \
	--description="Docker repository for microservices"
```

## 3. Build Docker Images

```bash
docker build -t iteminfod ./iteminfod
docker build -t stockinfod ./stockinfod
docker build -t aggregatord ./aggregatord
```

## 4. Tag Images for Artifact Registry

```bash
docker tag iteminfod us-west2-docker.pkg.dev/microservices-aggregator/microservices-repo/iteminfod:latest
docker tag stockinfod us-west2-docker.pkg.dev/microservices-aggregator/microservices-repo/stockinfod:latest
docker tag aggregatord us-west2-docker.pkg.dev/microservices-aggregator/microservices-repo/aggregatord:latest
```

## 5. Push Images to Artifact Registry

```bash
docker push us-west2-docker.pkg.dev/microservices-aggregator/microservices-repo/iteminfod:latest
docker push us-west2-docker.pkg.dev/microservices-aggregator/microservices-repo/stockinfod:latest
docker push us-west2-docker.pkg.dev/microservices-aggregator/microservices-repo/aggregatord:latest
```

## 6. Deploy Microservices to Cloud Run

```bash
gcloud run deploy iteminfod \
	--image us-west2-docker.pkg.dev/microservices-aggregator/microservices-repo/iteminfod:latest \
	--region us-west2 --port 8080 --allow-unauthenticated

gcloud run deploy stockinfod \
	--image us-west2-docker.pkg.dev/microservices-aggregator/microservices-repo/stockinfod:latest \
	--region us-west2 --port 8081 --allow-unauthenticated
```

Generates Service URLs:
- https://iteminfod-19495045139.us-west2.run.app/item-info
- https://stockinfod-19495045139.us-west2.run.app/stock-info


## 7. Deploy Aggregator to Cloud Run (with environment variables)
- VERY IMPORTANT: Set environment variables for our microservices URLs that aggregator needs to target its requests at.

```bash
gcloud run deploy aggregatord \
	--image us-west2-docker.pkg.dev/microservices-aggregator/microservices-repo/aggregatord:latest \
	--region us-west2 --port 8082 --allow-unauthenticated \
	--set-env-vars ITEMINFOD_URL=https://iteminfod-19495045139.us-west2.run.app/item-info,STOCKINFOD_URL=https://stockinfod-19495045139.us-west2.run.app/stock-info
```

## 8. Test with curl (replace with your actual aggregator URL)

```bash
curl -X POST "https://aggregatord-19495045139.us-west2.run.app/lookup" \
	-d '{"productID":"XYZ-12345"}' \
	-H "Content-Type: application/json"
```

Disable Services
- You should disable/remove services after testing/use
- You will have to redeploy them (steps 6-7) which also means redefining the service URL environment variables in (step 7)


Submission Testing

Final Aggregation
If Item Info = 404, return 404 to client. (No product.)If Item Info = 200 and Stock = 200, return merged information.If Item Info = 200 and Stock = 404, return 200 with  available: 0

## /clientd/client.py
- Feel free to simply run this file, as it includes the three test cases mentioned.

## Aggregator Endpoint Test Cases

**1. Item Info = 404 (No product)**
```sh
curl -i -X POST "https://aggregatord-19495045139.us-west2.run.app/lookup" \
  -d '{"productID":"NON_EXISTENT_ID"}' \
  -H "Content-Type: application/json"
```
_Expected: HTTP 404 response._

**2. Item Info = 200 and Stock = 200 (Merged information)**
```sh
curl -i -X POST "https://aggregatord-19495045139.us-west2.run.app/lookup" \
  -d '{"productID":"VALID_ID_WITH_STOCK"}' \
  -H "Content-Type: application/json"
```
_Expected: HTTP 200 response with merged item and stock info._

**3. Item Info = 200 and Stock = 404 (Available: 0)**
```sh
curl -i -X POST "https://aggregatord-19495045139.us-west2.run.app/lookup" \
  -d '{"productID":"VALID_ID_NO_STOCK"}' \
  -H "Content-Type: application/json"
```
_Expected: HTTP 200 response with item info and `"available": 0`._

Replace `NON_EXISTENT_ID`, `VALID_ID_WITH_STOCK`, and `VALID_ID_NO_STOCK` with actual product IDs for your test cases.
- Respectively, using our own dummy data: ABC-99999, XYZ-12345, RQY-22222



[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/W4tgy1bp)

